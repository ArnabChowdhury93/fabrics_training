CREATE TABLE [dbo].[credit_card_transactions] (

	[transaction_id] int NULL, 
	[transaction_ts] datetime2(6) NULL, 
	[card_number] varchar(8000) NULL, 
	[merchant_id] varchar(8000) NULL, 
	[amount] decimal(38,6) NULL, 
	[currency] varchar(8000) NULL, 
	[channel] varchar(8000) NULL, 
	[last_updated_ts] datetime2(6) NULL
);