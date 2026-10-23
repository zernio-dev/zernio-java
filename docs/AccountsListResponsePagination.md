

# AccountsListResponsePagination

Present on a paginated request: `{ page, limit, total, pages }` with page and limit, `{ limit, nextCursor }` with cursor paging (limit alone or cursor).

## oneOf schemas
* [AccountCursorPagination](AccountCursorPagination.md)
* [Pagination](Pagination.md)

## Example
```java
// Import classes:
import dev.zernio.model.AccountsListResponsePagination;
import dev.zernio.model.AccountCursorPagination;
import dev.zernio.model.Pagination;

public class Example {
    public static void main(String[] args) {
        AccountsListResponsePagination exampleAccountsListResponsePagination = new AccountsListResponsePagination();

        // create a new AccountCursorPagination
        AccountCursorPagination exampleAccountCursorPagination = new AccountCursorPagination();
        // set AccountsListResponsePagination to AccountCursorPagination
        exampleAccountsListResponsePagination.setActualInstance(exampleAccountCursorPagination);
        // to get back the AccountCursorPagination set earlier
        AccountCursorPagination testAccountCursorPagination = (AccountCursorPagination) exampleAccountsListResponsePagination.getActualInstance();

        // create a new Pagination
        Pagination examplePagination = new Pagination();
        // set AccountsListResponsePagination to Pagination
        exampleAccountsListResponsePagination.setActualInstance(examplePagination);
        // to get back the Pagination set earlier
        Pagination testPagination = (Pagination) exampleAccountsListResponsePagination.getActualInstance();
    }
}
```


