#include <fcntl.h>
#include <unistd.h>
#include <iostream>
using namespace std;

#include "query.h"
#include "driver.hpp"

#define	EXIT_FD_ERROR 126;

/**
 * Execute a driver created by driver-generator
 *
 * usage: execute-driver [driverFile]
 *        driverFile     path where the driver have been written
 *
 * See std output for debug information and stderr for error information
 *
 * Exit code: 0 Success
 *            1 Error
 *            126 Unable to open the camera device
 */
int main(int, const char **argv)
{
    const Driver *driver = read_driver(argv[1]);
    if (!driver)
        return EXIT_FAILURE;
    

    errno = 0;
    const int fd = open(driver->device, O_WRONLY);
    if (fd < 0 || errno)
    {
        fprintf(stderr, "ERROR: Cannot access to %s\n", driver->device);
        delete driver;
        return EXIT_FD_ERROR;
    }

    int result = set_uvc_query(fd, driver->unit, driver->selector, driver->size, driver->control);

    delete driver;
    close(fd);
    return result;
}