..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".
..  Some of the content in this section is adapted from
    http://www.cs.yale.edu/homes/aspnes/classes/223/notes.html
   
.. index:: static functions

Static functions and variables
==============================
By default, all functions are global; 
they can be used in any file of your program whether or not a declaration appears in a header file. 
To limit access to the
current file, declare a function or variable ``static``, like this:

.. code-block:: cpp

   // assume all these definitions are in a single file "foo.cpp"

   // static variable used by non-static functions
   static bool verbose = false;

   bool is_verbose() {
     return verbose;
   }

   // vprint could reside in another file
   void vprint (std::string message) {
     if (is_verbose()) {
       std::cout << message << '\n';
     }
   }
   // this function only works if it is the same file
   // as the one where verbose is defined
   void verbose_print (std::string message) {
     if (verbose) {
       std::cout << message << '\n';
     }
   }

   // local static function can only be called in this compilation unit
   static void helloHelper(void) {
     puts("hi!");
   }

   // anyone can call `hello`
   void hello(int repetitions) {
     for(int i = 0; i < repetitions; ++i) {
       helloHelper();
     }
   }

Similar to file static functions and variables, 
the keyword ``static`` can also be used inside functions.
Static variables are initialized only the first time the function is called,
for example:

.. code-block:: cpp


   size_t counter() {
     static size_t count = 0;
     return ++count;
   }

The first time ``counter`` is called, 
the variable ``count`` is initialized to zero.
Each call thereafter, ``count`` is increased by 1 and the new value is returned.

Another appropriate use of static variable in functions:
when defining a constant that should only be initialized once.
For example, our earlier ``too_small`` function, could be:

.. code-block:: cpp

   #include "area.h"

   bool too_small (int x, int y) {
     static const int min_size = 10;
     return area(x, y) < min_size; 
   }


Under very rare circumstances,
it may be useful to have a variable local to a function that persists from one function call to the next.
You can do so by declaring the variable static.
For example, here is a function that counts how many times it has been called:

.. code-block:: cpp

   // return the number of times the function has been called
   int counter(void) {
     static count = 0;
     return ++count; 
   }

Static local variables are stored in the same memory space as global variables. 
But they are only visible inside the function that declares them. 
This makes them slightly less troublesome than global variables;
there is no fear that some unrelated code elsewhere will quietly change their value.
Static variables are rarely used in practice, however,
because they do not work well in multi-threaded applications.

-----

.. admonition:: More to Explore

  - From: cppreference.com: 

    - :lang:`function declarations <function>`
    - :lang:`Static local variables <storage_duration#Static_local_variables>`

