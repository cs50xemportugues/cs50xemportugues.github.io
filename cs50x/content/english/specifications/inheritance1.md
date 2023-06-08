Lab 5: Inheritance
==================

<div class="alert" data-alert="warning" role="alert"><p>You are welcome to collaborate with one or two classmates on this lab, though it is expected that every student in any such group contribute equally to the lab.</p></div>

Simulate the inheritance of blood types for each member of a family.

    $ ./inheritance
    Child (Generation 0): blood type OO
        Parent (Generation 1): blood type AO
            Grandparent (Generation 2): blood type OA
            Grandparent (Generation 2): blood type BO
        Parent (Generation 1): blood type OB
            Grandparent (Generation 2): blood type AO
            Grandparent (Generation 2): blood type BO
    
    

Background
----------

A person’s blood type is determined by two alleles (i.e., different forms of a gene). The three possible alleles are A, B, and O, of which each person has two (possibly the same, possibly different). Each of a child’s parents randomly passes one of their two blood type alleles to their child. The possible blood type combinations, then, are: OO, OA, OB, AO, AA, AB, BO, BA, and BB.

For example, if one parent has blood type AO and the other parent has blood type BB, then the child’s possible blood types would be AB and OB, depending on which allele is received from each parent. Similarly, if one parent has blood type AO and the other OB, then the child’s possible blood types would be AO, OB, AB, and OO.

Getting Started
---------------

Open [VS Code](https://code.cs50.io/).

Start by clicking inside your terminal window, then execute `cd` by itself. You should find that its “prompt” resembles the below.

    $
    

Click inside of that terminal window and then execute

    wget https://cdn.cs50.net/2022/fall/labs/5/inheritance.zip
    

followed by Enter in order to download a ZIP called `inheritance.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!

Now execute

    unzip inheritance.zip
    

to create a folder called `inheritance`. You no longer need the ZIP file, so you can execute

    rm inheritance.zip
    

and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.

Now type

    cd inheritance
    

followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

    inheritance/ $
    

If all was successful, you should execute

    ls
    

and you should see `inheritance.c`.

If you run into any trouble, follow these same steps again and see if you can determine where you went wrong!

Understanding
-------------

Take a look at the distribution code in `inheritance.c`.

Notice the definition of a type called `person`. Each person has an array of two `parents`, each of which is a pointer to another `person` struct. Each person also has an array of two `alleles`, each of which is a `char` (either `'A'`, `'B'`, or `'O'`).

Now, take a look at the `main` function. The function begins by “seeding” (i.e., providing some initial input to) a random number generator, which we’ll use later to generate random alleles. The `main` function then calls the `create_family` function to simulate the creation of `person` structs for a family of 3 generations (i.e. a person, their parents, and their grandparents). We then call `print_family` to print out each of those family members and their blood types. Finally, the function calls `free_family` to `free` any memory that was previously allocated with `malloc`.

The `create_family` and `free_family` functions are left to you to write!
