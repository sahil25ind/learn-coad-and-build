#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void main(){

      char questions[][200] = {
          " 1. What is the correct syntax to print \"Hello, World!\" in C?",
          " 2. Which header file is required for input/output functions in C?",
          " 3. C is a _______ programming language.",
          " 4. The correct format specifier for printing an integer is:",
          " 5. What is the default return type of the main() function in C?",
          " 6. Which of the following is not a valid variable name in C?",
          " 7. The size of the int data type is typically:",
          " 8. Which of these is a floating-point data type in C?",
          " 9. What is the output of the following code?\n\tint a = 10, b = 20;\n\tprintf(\"%d\", a + b);",
          "10. What is the value of x after executing the following code?\n\tint x = 5;\n\tx += 10;",
          "11. What is the output of the following code?\n\tif (0)\n\tprintf(\"True\");\n\telse\n\tprintf(\"False\");",
          "12. Which of the following loops is guaranteed to execute at least once?",
          "13. How do you terminate a switch statement in C?",
          "14. Which keyword is used to skip the current iteration of a loop in C?",
          "15. What will be the output of the following code?\n\tint i;\n\tfor (i = 0; i < 5; i++);\n\tprintf(\"%d\", i);",
          "16. Which keyword is used to return a value from a function in C?",
          "17. What is the output of the following code?\n\tint fun(){\n\treturn 10;\n\t}\n\tprintf(\"%d\", fun());",
          "18. What is the correct way to declare a function that takes two int parameters and returns a float?",
          "19. What is recursion in C?",
          "20. What is the correct syntax for passing an array to a function in C?",
          "21. Which of the following is the correct syntax to declare a pointer in C?",
          "22. What does the & operator do in C?",
          "23. What is the output of the following code?\n\tint a = 10;\n\tint *p = &a;\n\tprintf(\"%d\", *p);",
          "24. Which of the following is not a valid operation on pointers?",
          "25. What will the following code output?\n\tint arr[] = {10, 20, 30};\n\tint *p = arr;\n\tprintf(\"%d\", *(p + 1));",
          "26. Which of the following is the correct syntax to declare an array in C?",
          "27. What is the index of the last element in an array of size 10?",
          "28. What is the correct syntax to include a header file in C?",
          "29. Which function is used to read a formatted input from the keyboard?",
          "30. C programs are converted into machine language using a:",
          "31. Which of the following is a valid escape sequence in C?",
          "32. Which of these is not a primitive data type in C?",
          "33. What will be the output of the following code?\n\tint a = 10 / 3;\n\tprintf(\"%d\", a);",
          "34. What is the range of values for a char data type in C?",
          "35. Which of the following data types can store a single character?",
          "36. What is the result of the expression 5 % 2 in C?",
          "37. Which operator has the highest precedence in C?",
          "38. What is the result of the following operation?",
          "39. What does the sizeof operator return in C?",
          "40. Which of these is a bitwise operator in C?",
          "41. How many times is the following loop executed?\n\tfor (int i = 0; i < 5; i++) { }",
          "42. What will be the output of this code?\n\tint x = 0;\n\tif (x)\n\t    printf(\"True\");\n\telse\n\t    printf(\"False\");",
          "43. What is the purpose of the default keyword in a switch statement?",
          "44. What is a null pointer in C?",
          "45. What is the correct way to declare a constant pointer in C?",
          "46. What is the output of the following code?",
          "47. Which function is used to concatenate two strings in C?",
          "48. What is the correct way to define a function that returns no value?",
          "49. Which of the following is not a valid storage class in C?",
          "50. Which function is used to open a file in C?",
          "51. Which mode is used to open a file for reading in C?",
          "52. What does the fclose() function do?",
          "53. What will be the result of the following declaration?\n\tint (*p)[5];",
          "54. Dynamic memory allocation in C is done using which function?",
          "55. Which of the following storage classes in C has the longest scope?",
          "56. Which keyword is used to prevent a variable from being modified?",
          "57. What does the keyword volatile indicate in C?",
          "58. Which of the following statements about static variables is true?",
          "59. Which of the following is not a valid operator in C?",
          "60. In which section of memory are local variables typically stored in C?",
          "61. What will happen if you access memory outside the bounds of an array in C?",
          "62. Which of the following is a valid definition of a typedef?",
          "63. What is the difference between calloc and malloc?",
          "64. What is the purpose of the union keyword in C?",
          "65. Which of the following best describes the function of a preprocessor directive in C?",
          "66. What is the primary purpose of the #define preprocessor directive?",
          "67. What is the correct way to prevent multiple inclusions of a header file in C?",
          "68. Which of the following statements about recursion is false?",
          "69. What is the difference between a structure and a union in C?",
          "70. Which function is used to position the file pointer at a specific location in C?",
          "71. What is a dangling pointer in C?",
          "72. What is the purpose of the extern keyword in C?",
          "73. Which of the following file modes is used to append data to an existing file in C?",
          "74. What is the primary difference between exit() and _exit() in C?",
          "75. Which of the following is true about NULL in C?",
          "76. Which memory allocation function in C automatically initializes the allocated memory to zero?",
          "77. What does the term \"segmentation fault\" refer to in C programming?",
          "78. Which library is commonly used in C for creating cross-platform GUIs?",
          "79. In 3D graphics programming, what does the term \"Z-buffering\" refer to?",
          "80. Which of the following best describes the role of OpenGL in 3D programming?",
          "81. What is the primary purpose of the glViewport function in OpenGL?",
          "82. What is a \"frame buffer\" in graphics programming?",
          "83. Which mathematical concept is most critical for transforming 3D coordinates into 2D screen coordinates?",
          "84. Which of the following libraries provides a physics engine suitable for use with C programming in games?",
          "85. What is the primary purpose of a \"vertex buffer object\" (VBO) in 3D rendering?",
          "86. In 3D particle simulations, what does the term \"particle emitter\" refer to?",
          "87. Which of the following best describes the role of a fragment shader in the graphics pipeline?",
          "88. In the context of game development, what is \"delta time\" used for?",
          "89. Which data structure is commonly used to implement spatial partitioning for collision detection in 3D games?",
          "90. What is the purpose of the \"model-view-projection\" (MVP) matrix in 3D rendering?",
          "91. In real-time 3D graphics, what is a \"shader program\"?",
          "92. What does the term \"back-face culling\" refer to in 3D rendering?",
          "93. In GUI programming using C, what does the event-driven programming model refer to?",
          "94. Which of the following tools or libraries is most commonly used for 2D and 3D game development in C?",
          "95. In 3D simulations, what is the role of a \"physics engine\"?",
          "96. What is \"double buffering\" in graphics rendering?",
          "97. Which of the following techniques is commonly used to create realistic motion in particle simulations?",
          "98. What is the primary purpose of the \"game loop\" in game programming?",
          "99. Which C library is often used to handle keyboard and mouse input in games?",
          "100. In 3D rendering, what is \"ray tracing\"?"
          };

    char options[][4][100] = {
        {"A) printf(\"Hello, World!\");","B) print(\"Hello, World!\");","C) cout << \"Hello, World!\";","D) System.out.println(\"Hello, World!\");"},
        {"A) <stdlib.h>","B) <stdio.h>","C) <string.h>","D) <conio.h>"},
        {"A) Low-level","B) High-level","C) Middle-level","D) None of the above"},
        {"A) %c","B) %d","C) %s","D) %f"},
        {"A) int","B) void","C) float","D) char"},
        {"A) variable_name","B) 1variable","C) variable1","D) _variable"},
        {"A) 1 byte","B) 2 bytes","C) 4 bytes","D) 8 bytes"},
        {"A) int","B) char","C) float","D) bool"},
        {"A) 10","B) 20","C) 30","D) Compilation Error"},
        {"A) 5","B) 10","C) 15","D) 50"},
        {"A) True","B) False","C) Compilation Error","D) Undefined Behavior"},
        {"A) for loop","B) while loop","C) do-while loop","D) None of the above"},
        {"A) stop","B) break","C) end","D) terminate"},
        {"A) break","B) continue","C) exit","D) skip"},
        {"A) 4","B) 5","C) 0","D) Compilation Error"},
        {"A) return","B) output","C) yield","D) export"},
        {"A) 10","B) Compilation Error","C) Undefined Behavior","D) None of the above"},
        {"A) float function(int a, b);","B) float function(int a, int b);","C) function float(int a, int b);","D) float function(a, b);"},
        {"A) A function that calls itself","B) A function that returns void","C) A function with no parameters","D) None of the above"},
        {"A) int fun(int arr[]);","B) int fun(int arr);","C) int fun(int *arr);","D) Both A and C"},
        {"A) int ptr*;","B) int *ptr;","C) ptr int*;","D) int ptr;"},
        {"A) It performs bitwise AND operation","B) It returns the address of a variable","C) It dereferences a pointer","D) It declares a pointer"},
        {"A) Address of a","B) 10","C) Value of p","D) Compilation Error"},
        {"A) Addition","B) Subtraction","C) Multiplication","D) Comparison"},
        {"A) 10","B) 20","C) 30","D) Compilation Error"},
        {"A) int arr[5];","B) int arr[] = {1, 2, 3};","C) int arr[5] = {0};","D) All of the above"},
        {"A) 9","B) 10","C) 11","D) Undefined"},
        {"A) #include \"header.h\"","B) #include <header.h>","C) Both A and B","D) None of the above"},
        {"A) printf()","B) scanf()","C) getchar()","D) gets()"},
        {"A) Compiler","B) Assembler","C) Interpreter","D) Linker"},
        {"A) \n","B) \t","C) \\","D) All of the above"},
        {"A) int","B) float","C) bool","D) char"},
        {"A) 3.33","B) 3","C) 10","D) Compilation Error"},
        {"A) -128 to 127","B) 0 to 255","C) -256 to 255","D) None of the above"},
        {"A) char","B) int","C) string","D) float"},
        {"A) 2.5","B) 2","C) 1","D) 0"},
        {"A) +","B) *","C) ()","D) ="},
        {"A) 1","B) 0","C) 5","D) Compilation Error"},
        {"A) The number of elements in an array","B) The size of a variable in bytes","C) The memory address of a variable","D) None of the above"},
        {"A) &&","B) ||","C) &","D) /"},
        {"A) 4","B) 5","C) 6","D) Infinite"},
        {"A) True","B) False","C) 0","D) Compilation Error"},
        {"A) To terminate the switch statement","B) To execute code when no case matches","C) To declare a variable","D) None of the above"},
        {"A) A pointer pointing to a valid memory location","B) A pointer that is not initialized","C) A pointer with the value 0","D) A pointer pointing to an array"},
        {"A) const int *ptr;","B) int const *ptr;","C) int *const ptr;","D) All of the above"},
        {"A) Hello","B) H","C) Compilation Error","D) None of the above"},
        {"A) strcat()","B) strcpy()","C) strcmp()","D) strlen()"},
        {"A) void functionName();","B) int functionName();","C) float functionName();","D) None of the above"},
        {"A) auto","B) register","C) volatile","D) static"},
        {"A) fileopen()","B) openfile()","C) fopen()","D) open()"},
        {"A) \"w\"","B) \"r\"","C) \"rw\"","D) \"r+\""},
        {"A) Flushes the buffer to a file","B) Closes an open file","C) Deletes a file","D) None of the above"},
        {"A) Pointer to an array of integers","B) Array of 5 pointers","C) Compilation Error","D) None of the above"},
        {"A) malloc()","B) new","C) calloc()","D) Both A and C"},
        {"A) auto","B) register","C) static","D) extern"},
        {"A) static","B) volatile","C) const","D) extern"},
        {"A) The value of the variable may change unexpectedly.","B) The variable is constant and cannot be modified.","C) The variable is stored in CPU registers.","D) The variable is global."},
        {"A) They have a local scope and their lifetime is limited to the function in which they are defined.","B) They have a local scope but retain their value between function calls.","C) They are global variables by default.","D) They are always initialized to zero."},
        {"A) sizeof","B) ?:","C) >>","D) and"},
        {"A) Stack","B) Heap","C) Data Segment","D) Code Segment"},
        {"A) Compilation error","B) Runtime error","C) Undefined behavior","D) The program will crash immediately"},
        {"A) typedef unsigned int UINT;","B) typedef int unsigned UINT;","C) typedef UINT unsigned int;","D) unsigned typedef int UINT;"},
        {"A) malloc initializes memory to zero, calloc does not.","B) calloc initializes memory to zero, malloc does not.","C) calloc requires a pointer, malloc does not.","D) There is no difference."},
        {"A) To group multiple variables of different types and allocate memory equal to the size of the largest member.","B) To create a collection of variables of the same type.","C) To enable polymorphism in C.","D) To encapsulate variables and functions together."},
        {"A) It is used to declare global variables.","B) It is executed during the program's runtime.","C) It provides instructions to the compiler before the program is compiled.","D) It allocates memory dynamically."},
        {"A) To define functions.","B) To define constants or macros.","C) To include header files.","D) To declare variables."},
        {"A) Using #endif","B) Using #ifndef and #define","C) Using #pragma once","D) Both B and C"},
        {"A) Recursion requires a base condition to terminate.","B) Excessive recursion may lead to stack overflow.","C) Recursive functions always execute faster than iterative ones.","D) Recursion can be replaced by iteration in most cases."},
        {"A) Structures allocate memory for all members, whereas unions allocate memory for the largest member only.","B) Structures allocate memory for the largest member only, whereas unions allocate memory for all members.","C) Structures and unions are identical.","D) None of the above."},
        {"A) fseek()","B) rewind()","C) ftell()","D) feof()"},
        {"A) A pointer that is initialized but not used.","B) A pointer that has been deallocated but still points to a memory location.","C) A pointer pointing to the start of an array.","D) A pointer with a NULL value."},
        {"A) To define a global variable.","B) To declare a variable without defining it.","C) To allocate memory dynamically.","D) To mark a variable as constant."},
        {"A) \"w\"","B) \"r+\"","C) \"a\"","D) \"w+\""},
        {"A) exit() flushes all open file streams, while _exit() does not.","B) _exit() flushes all open file streams, while exit() does not.","C) There is no difference.","D) Both terminate the program abnormally."},
        {"A) It is the same as 0.","B) It is used to represent a null character.","C) It represents an invalid memory location.","D) Both A and C."},
        {"A) malloc()","B) calloc()","C) realloc()","D) None of the above"},
        {"A) A syntax error in the program.","B) An error when accessing memory outside the program's allocated region.","C) A compiler warning for unused variables.","D) A runtime error due to type mismatches."},
        {"A) GTK+","B) OpenCV","C) OpenGL","D) SDL"},
        {"A) A technique to optimize CPU usage.","B) A data structure used to store depth information to handle occlusion.","C) A method to reduce memory usage during particle simulation.","D) A technique to enhance image resolution."},
        {"A) It is a physics engine used for collision detection.","B) It is a low-level graphics API used for rendering 2D and 3D objects.","C) It is a compiler extension for 3D simulations.","D) It is a sound library for 3D games."},
        {"A) To define the area of the screen where rendering will occur.","B) To initialize shaders for 3D rendering.","C) To allocate memory for particle simulation.","D) To optimize rendering pipelines."},
        {"A) A temporary storage area that holds pixel data for a single frame.","B) A library function that controls rendering pipelines.","C) A mathematical model used for object transformations.","D) A method to optimize collision detection."},
        {"A) Matrix multiplication","B) Fourier transform","C) Discrete cosine transform","D) Hashing"},
        {"A) Bullet Physics","B) GLFW","C) FreeType","D) GLEW"},
        {"A) To store vertex data in GPU memory for efficient rendering.","B) To allocate memory for texture coordinates.","C) To handle collision detection.","D) To initialize light sources in a scene."},
        {"A) A source that continuously generates particles with specific attributes.","B) A function that renders 3D models in real-time.","C) A data structure used for sorting particles by size.","D) A shader program for managing lighting effects."},
        {"A) It determines the final color of each pixel.","B) It computes transformations for vertices.","C) It simulates particle movement.","D) It handles collision physics."},
        {"A) To calculate the time difference between frames for smooth movement.","B) To manage memory allocation in real-time.","C) To optimize multi-threading in the physics engine.","D) To measure the rendering time of shaders."},
        {"A) Quadtree","B) Octree","C) Linked List","D) Red-Black Tree"},
        {"A) To combine object transformations, camera positioning, and projection into a single matrix.","B) To allocate GPU resources dynamically.","C) To optimize Z-buffer algorithms.","D) To reduce the computational cost of texture mapping."},
        {"A) A program written in GLSL or HLSL that runs on the GPU for custom rendering effects.","B) A debugging tool for tracking rendering performance.","C) A compiler extension for optimizing binary executables.","D) A memory management utility in physics simulations."},
        {"A) A technique to discard faces of objects that are not visible to the camera.","B) A method to optimize memory usage for large textures.","C) A rendering technique to prioritize near objects.","D) A function to manage occlusion queries."},
        {"A) A programming paradigm where the flow of the program is determined by user interactions or other events.","B) A multi-threading model for optimizing GUI performance.","C) A real-time simulation framework for 3D interactions.","D) A method to allocate memory dynamically for GUI components."},
        {"A) SDL","B) DirectX","C) Vulkan","D) All of the above"},
        {"A) To simulate real-world physical behavior, such as collisions, gravity, and friction.","B) To optimize the rendering pipeline for large textures.","C) To calculate lighting effects for complex scenes.","D) To manage the interaction between shaders and GPU memory."},
        {"A) Using two buffers to reduce flickering during rendering.","B) Allocating twice the memory for high-resolution textures.","C) Simultaneously rendering two frames for parallel processing.","D) A technique to optimize particle simulations."},
        {"A) Perlin noise","B) Depth buffering","C) Back-face culling","D) Bilinear interpolation"},
        {"A) To continuously update the game state and render frames.","B) To initialize game assets and resources.","C) To manage memory allocation for game objects.","D) To detect collisions between game entities."},
        {"A) SDL","B) OpenAL","C) GLFW","D) GLEW"},
        {"A) A technique to simulate realistic light behavior by tracing rays.","B) A method to optimize the rendering pipeline for large datasets.","C) A physics engine used for collision detection.","D) A technique for mapping textures onto 3D surfaces."},
        };
        char answers[] = {'A','B','C','B','A','B','C','C','C','C','B','C','B','B','B','A','A','B','A','D','B','B','B','C','B','D','A','C','B','A','D',
        'C','B','A','A','C','C','B','B','C','B','B','B','C','D','A','A','A','C','C','B','B','A','D','D','C','A','B','D','A','C','A','B','A','C','B',
        'D','C','A','A','B','B','C','A','D','B','B','A','B','B','A','A','A','A','A','A','A','A','B','A','A','A','A','D','A','A','A','A','C','A'};

        int sizeofquestions = sizeof(questions)/sizeof(questions[0]);
        int sizeofoptions = sizeof(options[0])/sizeof(options[0][0]);
        char guesses[sizeofquestions];
        int correctlyanswered = 0;
        double mark;
        int marks;

        //answers of all the question in perfect order(arranged)
        printf("abcbabccccbcbbbaabadbbbcbdacbadcbaaccbbcbbbcdaaaccbbaddcabdacabacbdcaabbcadbbabbaaaaaaaabaaaadaaaaca\n");
        printf("********** Quiz Game in C **********\n");

        for(int i = 0;i<sizeofquestions;i++){
            printf("--------------------------------------------------------------------------------\n");
            printf("%s \n",questions[i]);
            for(int j = 0;j<sizeofoptions;j++){
                printf("%s \n",options[i][j]);
            }
            printf("\nEnter Your Answer (A, B, C, D): ");
            scanf(" %c",&guesses[i]);
            guesses[i] = toupper(guesses[i]);

            if(guesses[i] == answers[i]){
                printf("Correct Answer!\n");
                correctlyanswered++;
            }else{
                printf("Wrong Answer!\n");
                printf("Correct answer is: %c \n",answers[i]);
            }
        }

        mark = ((float)correctlyanswered / sizeofquestions)*100;
        marks = (int)mark;

        printf("--------------------------------------------------------------------------------\n");
        printf("            RESULT               \n");
        printf("--------------------------------------------------------------------------------\n");

        printf("Total correctly answered: %4d\n",correctlyanswered);
        printf("SCORE: %3d/%3d     MARKS: %3d%%\n",correctlyanswered,sizeofquestions,marks);

        printf("--------------------------------------------------------------------------------\n");

        system("pause");
}

