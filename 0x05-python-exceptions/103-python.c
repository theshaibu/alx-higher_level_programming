#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <stdlib.h>
#include <float.h>

void display_python_float_info(PyObject *object) {
    PyFloatObject *floatObj = (PyFloatObject *)object;
    double value = floatObj->ob_fval;
    char *stringRepresentation = NULL;

    printf("[.] Information about the float object\n");
    if (!PyFloat_Check(floatObj)) {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    stringRepresentation = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
    printf("  value: %s\n", stringRepresentation);
}

void display_python_bytes_info(PyObject *object) {
    long unsigned int size;
    unsigned int i;
    char *stringData = NULL;

    printf("[.] Information about the bytes object\n");
    if (!PyBytes_Check(object)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)object)->ob_size;
    stringData = ((PyBytesObject *)object)->ob_sval;
    printf("  size: %lu\n", size);
    printf("  data: %s\n", stringData);
    if (size < 10)
        printf("  first %lu bytes:", size + 1);
    else
        printf("  first 10 bytes:");
    for (i = 0; i <= size && i < 10; i++)
        printf(" %02hhx", stringData[i]);
    printf("\n");
}

void display_python_list_info(PyObject *object) {
    long unsigned int size;
    unsigned int i;
    PyListObject *listObject = (PyListObject *)object;
    const char *elementType;

    printf("[*] Information about the Python list\n");
    if (!PyList_Check(listObject)) {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = ((PyVarObject *)object)->ob_size;
    printf("[*] Size of the Python List = %lu\n", size);
    printf("[*] Allocated = %lu\n", listObject->allocated);
    for (i = 0; i < size; i++) {
        elementType = (listObject->ob_item[i])->ob_type->tp_name;
        printf("Element %i: %s\n", i, elementType);
        if (!strcmp(elementType, "bytes"))
            display_python_bytes_info(listObject->ob_item[i]);
        if (!strcmp(elementType, "float"))
            display_python_float_info(listObject->ob_item[i]);
    }
}

