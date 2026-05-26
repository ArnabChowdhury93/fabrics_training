CREATE PROCEDURE update_watermark_table
    @lastmodifytime DATETIME2(6),
    @TableName      VARCHAR(40)
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE watermark_control
    SET last_watermark = @lastmodifytime
    WHERE pipeline_name = @TableName;
END;