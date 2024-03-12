#!/usr/bin/node
// a class Rectangle that defines a rectangle:

class Rectangle {
    constructor(w, h) {
        if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
            // Create an empty object if w or h is equal to 0 or not a positive integer
            return {};
        } else {
            // Initialize instance attributes width and height with the provided values
            this.width = w;
            this.height = h;
        }
    }
}

module.exports = Rectangle;
