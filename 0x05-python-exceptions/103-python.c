#include <stdio.h>
#include <Python.h>

void print_python_list(PyObject *p)
{
    if (!PyList_Check(p)) {
        printf("[ERROR] Invalid PyListObject\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        PyObject *element = PyList_GetItem(p, i);
        const char *element_type = Py_TYPE(element)->tp_name;

        printf("Element %zd: %s\n", i, element_type);
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("[ERROR] Invalid PyBytesObject\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    Py_ssize_t i;
    char *bytes = PyBytes_AsString(p);

    printf("[*] Python bytes info\n");
    printf("[*] Size of the Python Bytes = %zd\n", size);
    printf("Bytes: ");
    for (i = 0; i < size && i < 10; i++) {
        printf("%02x ", (unsigned char)bytes[i]);
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        printf("[ERROR] Invalid PyFloatObject\n");
        return;
    }

    double value = PyFloat_AsDouble(p);

    printf("[*] Python float info\n");
    printf("[*] Value: %f\n", value);
}
