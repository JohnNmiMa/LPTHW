This section of the PIP course was on learning OO in Python.
The project here models the building of automobiles.
There is a class called Automobile that knows how to build a
generic car. In the class is a Template Method named 'build()'
that implements an algorithm that correctly builds
automobiles - each stage done in the correct order.
Each stage of building and assembling a car is represented as
a method call in the template. The Automobile class can be
subclassed so that other more specialized cars can be built.
The SportsCar class is such a class.

The building of a car can be done one step after another in a
serial fashion, or in parallel. The threading.Thread object is
used to create and control the threads. To help pace each stage
of the car the threading.Event class was used. When one stage is
dependent upon a previous stage to be complete, the dependent stage
will wait() upon the previous stage until an event is set/signaled.

Each stage has a set amount of time to complete, and is specified
in hours. To help build the automobile sooner than real-time,
a rate factor can be specified so that the car will be built in
seconds, rather than days.

The project was done in TDD fashion, producing a failing test, and
then makeing it pass, and then refactoring the code as needed.
