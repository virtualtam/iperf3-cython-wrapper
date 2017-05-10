cdef extern from "iperf_api.h":
    cdef struct iperf_test:
        pass

    iperf_test *iperf_new_test()
    int iperf_defaults(iperf_test *testp)

def main():
    cdef iperf_test *testp
    testp = iperf_new_test()
    iperf_defaults(testp)

if __name__ == '__main__':
    main()
