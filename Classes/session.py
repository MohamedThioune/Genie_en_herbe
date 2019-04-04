class Session:
    def __init__(self, idmail, iddate,perfid,heureConnect,heureDeConnect):
        self._idmail = idmail
        self._iddate = iddate
        self._perfid = perfid
        self._heureConnect = heureConnect
        self._heureDeconnect = heureDeConnect

    def _get_idmail(self):
        return self._idmail

    def _set_idmail(self, news_values):
        self._idmail = news_values

    def _get_iddate(self):
        return self._iddate

    def _set_iddate(self, news_values):
        self._iddate = news_values

    def _get_perfid(self):
        return self._perfid

    def _set_perfid(self, news_values):
        self._perfid = news_values

    def _get_heureConnect(self):
        return self._heureConnect

    def _set_heureConnect(self, news_values):
        self._heureDeconnect = news_values

    def _get_heureDeconnect(self):
        return self._heureDeconnect

    def _set_heureDeconnect(self, news_values):
        self._heureDeconnect = news_values

    def __repr__(self):
        return "|Session|\n m@il: {}\n date [id]: {}\n performance [id]: {}\n heure connection : {}\n heure deconnection: {}".format(self._idmail,
                                                                                                       self._iddate,
                                                                                                       self._perfid,
                                                                                                       self._heureConnect,
                                                                                                       self._heureDeconnect)

    idmail = property(_get_idmail, _set_idmail)
    iddate = property(_get_iddate, _set_iddate)
    perfid = property(_get_perfid, _set_perfid)
    heureConnect = property(_get_heureConnect, _set_heureConnect)
    heureDeconnect = property(_get_heureDeconnect, _set_heureDeconnect)

