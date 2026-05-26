CREATE FUNCTION dbo.fn_region_access(@region AS VARCHAR(50))
RETURNS TABLE
WITH SCHEMABINDING
AS
RETURN
SELECT 1 AS access_result
WHERE @region IN
(
    SELECT region
    FROM dbo.region_security
    WHERE user_email = USER_NAME()
);