class APIException(Exception):
    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code
        super().__init__(message)

class TableNotFoundException(APIException):
    def __init__(self, table_id: int):
        super().__init__(
            message=f"Table with id {table_id} not found",
            status_code=404
        )

class ReservationNotFoundException(APIException):
    def __init__(self, reservation_id: int):
        super().__init__(
            message=f"Reservation with id {reservation_id} not found",
            status_code=404
        )

class ReservationConflictException(APIException):
    def __init__(self):
        super().__init__(
            message="Time slot already booked",
            status_code=409
        )

class PastReservationException(APIException):
    def __init__(self):
        super().__init__(
            message="Cannot create reservation in the past",
            status_code=400
        )