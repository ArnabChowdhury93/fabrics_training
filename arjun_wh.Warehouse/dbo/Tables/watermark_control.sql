CREATE TABLE [dbo].[watermark_control] (

	[pipeline_name] varchar(50) NULL, 
	[last_watermark] datetime2(6) NULL
);