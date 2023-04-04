class ConsertRepositroy:

    def create(self, id: int, name: str, date: datetime, comment: str,
               location: int, orgnizer: int, price_str: str, time_str: str,
               type: int):

        self.id = id
    self.name = name
    self.c_date = date
    self.comment = comment
    self.location = location
    self.orgnizer = orgnizer
    self.price_str = price_str
    self.time_str = time_str
    self.type = type

    def get_id(self) -> int:
        return self.id

    def get_conserts():
        consert_df = conn.get_konsert()
        return consert_df

    def get_konserts():
        connection = conn.connect()
        konsert_df = pd.read_sql('select * from Konsert order by ID', conn,
                                 index_col=None)
        return konsert_df
