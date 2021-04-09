# distutils: language = c++
from cython.operator cimport dereference

cdef extern from "req.h" namespace 'cstuff':
    cdef cppclass Request[Loc]:
        int request_id
        double creation_timestamp

        Request()
        Request(int, double)

cdef class IntRequest:
    cdef Request[int] creq

    def __init__(
            self,
            int request_id,
            float creation_timestamp,
        ):
        self.creq = Request[int](
            request_id, creation_timestamp
        )

    def asdict(self):
        return dict(
            request_id=(self.creq).request_id,
            creation_timestamp=(self.creq).creation_timestamp,
        )

    def __repr__(self):
        return f"{self.__class__.__name__}(" + ", ".join(f"{k}={v}" for k, v in self.asdict().items()) + ")"
