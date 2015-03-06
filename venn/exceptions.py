class VennError(Exception):
    """ Exception for Venn API Errors """
    def __init__(self, response):
        self.code = response.status_code
        try:
            self.message = response.json().get("message", "Unknown Error")
        except ValueError:
            self.message = "Unknown Error"
        message = "[{}] {}".format(self.code, self.message)
        super(VennError, self).__init__(message)
