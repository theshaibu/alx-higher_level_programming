#include <Python.h>

void print_python_string(PyObject *p) {
    // Check if the object is a string
    if (!PyUnicode_Check(p)) {
        PyErr_SetString(PyExc_TypeError, "Expected a string");
        return;
    }

    // Get the C string from the Python object
    const char *str = PyUnicode_AsUTF8(p);

    // Check if conversion was successful
    if (!str) {
        PyErr_SetString(PyExc_RuntimeError, "Unable to convert string");
        return;
    }

    // Print the C string
    printf("%s\n", str);
}

int main() {
    // Initialize the Python interpreter
    Py_Initialize();

    // Example usage
    PyObject *string_obj = PyUnicode_FromString("Hello, Python Strings!");
    print_python_string(string_obj);

    // Don't forget to cleanup
    Py_DECREF(string_obj);

    // Finalize the Python interpreter
    Py_Finalize();

    return 0;
}

