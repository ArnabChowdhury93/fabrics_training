[StagingDefinition = [Kind = "FastCopy"]]
section Section1;
[IncrementalRefreshSettings = [FilterColumnName = "last_updated_ts", WindowSize = 2, WindowUnit = "Year", BucketUnit = "Year", BookmarkColumnName = "last_updated_ts", ConsiderOnlyConcludedPeriods = false, RequireIncrementalRefreshQueryToFold = true], DataDestinations = {[Definition = [Kind = "Reference", QueryName = "credit_card_transactions_DataDestination", IsNewTarget = true], Settings = [Kind = "Manual", AllowCreation = true, ColumnSettings = [Mappings = {[SourceColumnName = "transaction_id", DestinationColumnName = "transaction_id"], [SourceColumnName = "transaction_ts", DestinationColumnName = "transaction_ts"], [SourceColumnName = "card_number", DestinationColumnName = "card_number"], [SourceColumnName = "merchant_id", DestinationColumnName = "merchant_id"], [SourceColumnName = "amount", DestinationColumnName = "amount"], [SourceColumnName = "currency", DestinationColumnName = "currency"], [SourceColumnName = "channel", DestinationColumnName = "channel"], [SourceColumnName = "last_updated_ts", DestinationColumnName = "last_updated_ts"]}], DynamicSchema = false, UpdateMethod = [Kind = "Replace"], TypeSettings = [Kind = "Table"]]]}]
shared credit_card_transactions = let
  Source = FabricSql.Contents(null),
  Navigation = Source{[workspaceId = "b79aed05-325a-458e-8274-26078b75c2ff"]}[Data],
  #"Navigation 1" = Navigation{[sqlId = "381af9cf-ff8b-418d-a769-feb62befe50a"]}[Data],
  #"Navigation 2" = #"Navigation 1"{[Schema = "dbo", Item = "credit_card_transactions"]}[Data]
in
  #"Navigation 2";
shared credit_card_transactions_DataDestination = let
  Pattern = Fabric.Warehouse([CreateNavigationProperties = false, HierarchicalNavigation = true]),
  Navigation_1 = Pattern{[workspaceId = "."]}[Data],
  Navigation_2 = Navigation_1{[displayName = "retail_warehouse"]}[Data],
  Navigation_3 = Navigation_2{[Schema = "dbo"]}[Data],
  TableNavigation = Navigation_3{[Name = "credit_card_transactions"]}?[Data]?
in
  TableNavigation;
