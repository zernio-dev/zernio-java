#!/usr/bin/env python3
"""Rewrite anyOf/oneOf unions openapi-generator cannot express in Java.

The Java generator emits a wrapper class per composed schema whose branch types
are pasted into identifiers (`getList<String>()`, `List<String>.class`), so any
branch that maps to a generic Java type produces source that does not parse.
Branches that map to a plain class are fine, and so is the `type: "null"` branch
every nullable field uses, which the generator strips.

Such unions are collapsed to a free-form schema (Java `Object`, which Jackson
still deserializes into the right runtime shape) instead of failing the build.
"""

import sys

import yaml

COMPOSED_KEYWORDS = ("anyOf", "oneOf")


def maps_to_generic_java_type(branch):
    if not isinstance(branch, dict):
        return False
    types = branch.get("type")
    types = types if isinstance(types, list) else [types]
    return "array" in types or bool(branch.get("additionalProperties"))


def is_null_branch(branch):
    return isinstance(branch, dict) and branch.get("type") == "null"


def collapse_unexpressible_unions(node, path, collapsed):
    if isinstance(node, list):
        for index, item in enumerate(node):
            collapse_unexpressible_unions(item, f"{path}[{index}]", collapsed)
        return

    if not isinstance(node, dict):
        return

    for keyword in COMPOSED_KEYWORDS:
        branches = node.get(keyword)
        if not isinstance(branches, list):
            continue
        typed = [b for b in branches if not is_null_branch(b)]
        if len(typed) > 1 and any(maps_to_generic_java_type(b) for b in typed):
            del node[keyword]
            collapsed.append(f"{path}.{keyword}")

    for key, value in node.items():
        collapse_unexpressible_unions(value, f"{path}.{key}", collapsed)


def main():
    source, destination = sys.argv[1], sys.argv[2]
    spec = yaml.safe_load(open(source))

    collapsed = []
    collapse_unexpressible_unions(spec, "$", collapsed)

    with open(destination, "w") as out:
        yaml.safe_dump(spec, out, sort_keys=False, allow_unicode=True, width=10**9)

    for location in collapsed:
        print(f"collapsed to free-form (unexpressible in Java): {location}")
    print(f"{len(collapsed)} union(s) collapsed -> {destination}")


if __name__ == "__main__":
    main()
