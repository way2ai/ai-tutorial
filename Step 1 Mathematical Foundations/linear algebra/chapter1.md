## Chapter 1: Systems of Linear Equations: Algebra

> **Primary Goal:** Solve a system of linear equations algebraically in parametric form.

### 1.1 Systems of Linear Equations

> **Definition:** An equation in the unknowns x,y,z,... is called linear if both sides of equation are a sum of (constant) multiples of x,y,z,..., plus an optional constant.

For instance:
$$
3x + 4y = 2z \\
-x - z = 100
$$

We will usually move the unknowns to the left side of the equation, and move the constants to the right.
$$
3x + 4y - 2z = 0 \\
-x - z = 100
$$

**A system of linear equations** is a collection of serveral linear equations, like
$$
\begin{cases}
\begin{aligned}
x + 2y + 3z &= 6 \\
2x - 3y + 2z &= 14 \\
3x + y - z &= -2
\end{aligned}
\end{cases}
$$

> Definition (Solution sets):
- **A solution** of a system of equations is a list of numbers x,y,z,... that make all of equations true simultaneously.
- The **solution set** of a system of equations is the collection of all solutions.
- **Solving** the system means finding all solutions with formulas involving some number of parameters.

A system of linear equations need not have a solution. In this case:
$$
\begin{cases}inconsistent
\begin{aligned}
x + 2y =3 \\
x + 2y = -3
\end{aligned}
\end{cases}
$$
It has its own name.

> Definition: A system of equations is called **inconsistent** if it has no solutions. It is called **consistent** otherwise.

R denote the set if all real numbers, i.e., the number line.

> Definition: Let n be a positive whole number. We define
$$
\mathbb
{R}^n = \text{all ordered } n\text{-tuples of real numbers } (x_1, x_2, x_3, \dots, x_n).
$$
An n-tuple of real numbers is called **a point of $\mathbb{R}^n$**.<p>

The number line: $\mathbb{R}$<p>
The Euclidean plane (xy-plane): $\mathbb{R}^2$<p>
3-Space: $\mathbb{R}^3$<p>


### 1.2 Row Reduction 行简化

#### Objectives 目标
1. Learn to replace a system of linear equations by an augmented(增广的) matrix(矩阵).
2. Learn how the elimination(消除) method corresonds(对应) to performing row opeaations on an augmented matrix.
3. Understand when a matrix is in (reduced) row echelon(阶梯) form.
4. Learn which row reduced matrices come from inconsistent(不相容，表示无解) linear systems.
5. Recipe(方法): the row reduction algorithm.
6. Vocabulary words(术语): **_row operation,row equivalence(等价),matrix,augmented matix,pivot(主元),(reduced) row echelon(阶梯) form_**.

#### The elimination Method(消元法)
We will solve systems of linear equations algebraically using the elimination method. In other words, we will combine the equations in various ways to try to eliminate as many variables as possible from each equation. There are three valid operations we can perform on our system of equations:

- **Scaling(缩放):** we can multiply both side of an equation by an nonzero number.
$$
\left\{
\begin{aligned}
x + 2y + 3z &= 6 \\
2x - 3y + 2z &= 14 \\
3x + y - z &= -2
\end{aligned}
\right.
\xrightarrow{\text{multiply 1st by } -3}
\left\{
\begin{aligned}
-3x - 6y - 9z &= -18 \\
2x - 3y + 2z &= 14 \\
3x + y - z &= -2
\end{aligned}
\right.
$$
- **Replacement(替换):** we can add a multiple of one equation to another, replacing the second equation with the result.
$$
\left\{
\begin{aligned}
x + 2y + 3z &= 6 \\
2x - 3y + 2z &= 14 \\
3x + y - z &= -2
\end{aligned}
\right.
\xrightarrow{\text{2nd} = \text{2nd} - 2 \times \text{1st}}
\left\{
\begin{aligned}
x + 2y + 3z &= 6 \\
-7y - 4z &= 2 \\
3x + y - z &= -2
\end{aligned}
\right.
$$
- **Swap(交换):** we can swap two equations.
$$
\left\{
\begin{aligned}
x + 2y + 3z &= 6 \\
2x - 3y + 2z &= 14 \\
3x + y - z &= -2
\end{aligned}
\right.
\xrightarrow{\text{3rd} \longleftrightarrow \text{1st}}
\left\{
\begin{aligned}
3x + y - z &= -2 \\
2x - 3y + 2z &= 14 \\
x + 2y + 3z &= 6
\end{aligned}
\right.
$$

#### Augmented Matix 增广矩阵

 Solving equations by elimination requires writing the variables x,y,z and the equals sign = over and over again, merely as placeholders: all that is changing in the equations is the coefficient numbers. We can make our life easier by extracting only the numbers, and putting them in a box:

$$
\left\{
\begin{aligned}
x + 2y + 3z &= 6 \\
2x - 3y + 2z &= 14 \\
3x + y - z &= -2
\end{aligned}
\right.
\xrightarrow{\text{becomes}}
\left(
\begin{array}{ccc|c}
1 & 2 & 3 & 6 \\
2 & -3 & 2 & 14 \\
3 & 1 & -1 & -2
\end{array}
\right).
$$

This is called an augmented matrix. The word “augmented” refers to the vertical line, which we draw to remind ourselves where the equals sign belongs; a matrix is a grid of numbers without the vertical line.

### Echelon Forms(阶梯式)

> **Definition.** A matrix is in **_row echelon form_** if:
> 1. All zero rows are at the bottom.
> 2. The first nonzero entry(元素) of a row is to thr right of the first nonzero entry of the row above.
> 3. Below the first nonzero entry of a row, all entries are zero.

Here is a picture of a matrix in row echelon form:
$$
\left(
\begin{array}{ccccc}
\boxed{\star} & \star & \star & \star & \star \\
0 & \boxed{\star} & \star & \star & \star \\
0 & 0 & 0 & \boxed{\star} & \star \\
0 & 0 & 0 & 0 & 0
\end{array}
\right)
\quad
\begin{aligned}
\star &= \text{any number} \\
\boxed{\star} &= \text{any nonzero number}
\end{aligned}
$$

> **Definition.** A **_pivot_** is the first nonzero entry of a row of a matrix in row echelon form.

A matrix in row-echelon form is generally easy to solve using back-substitution. For example,

> **Definition.** A matrix is in reduced row echelon form if it is in row echelon form, and in addition:
> - Each pivot is equal to 1.
> - Each pivot is the only nonzero entry in its column.

Here is a picture of a matrix in reduced row echelon form:
$$
\left(
\begin{array}{ccccc}
\boxed{1} & 0 & \star & 0 & \star \\
0 & \boxed{1} & \star & 0 & \star \\
0 & 0 & 0 & \boxed{1} & \star \\
0 & 0 & 0 & 0 & 0
\end{array}
\right)
\quad
\begin{aligned}
\star &= \text{any number} \\
\boxed{1} &= \text{pivot}
\end{aligned}
$$

A matrix in reduced row echelon form is in some sense completely solved. For example,
$$
\left\{
\begin{array}{ccc|c}
1 & 0 & 0 &= 1 \\
0 & 1 & 0 &= -2 \\
0 & 0 & 1 &= 3
\end{array}
\right.
\xrightarrow{\text{becomes}}
\left\{
\begin{aligned}
x &= 1 \\
y &= -2 \\
z &= 3
\end{aligned}
\right.
$$

#### The Row Reduction Algorithm(行简化算法)

> **Theorem(定理).** Every matrix is row equivalent to one and only one matrix in reduced row echelon form.
每个矩阵都行等价于一个且仅有一个约化行阶梯形矩阵

We will give an algorithm, called **_row reduction_** or **_Gaussian(高斯) elimination_**, which demonstrates that every matrix is row equivalent to at least one matrix in reduced row echelon form.

> Algorithm(Row Reduction)
>- Step 1a: Swap the 1st row with a lower one so a leftmost nonzero entry is in the 1st >- row (if necessary).
>- Step 1b: Scale the 1st row so that its first nonzero entry is equal to 1.
>- Step 1c: Use row replacement so all entries below this 1 are 0.
>- Step 2a: Swap the 2nd row with a lower one so that the leftmost nonzero entry is in the 2nd row.
>- Step 2b: Scale the 2nd row so that its first nonzero entry is equal to 1.
>- Step 2c: Use row replacement so all entries below this 1 are 0.
>- Step 3a: Swap the 3rd row with a lower one so that the leftmost nonzero entry is in the 3rd row.
> - etc.
>- Last Step: Use row replacement to clear all entries above the pivots, starting with the last pivot.

Here is the row reduction algorithm, summarized in pictures.
$$
\begin{array}{ccc}
\text{\color{blue}Get a 1 here} & \text{\color{blue}Clear down} & \text{\color{blue}Get a 1 here} \\
\left(\begin{array}{cccc}
\boxed{\star} & \star & \star & \star \\
\star & \star & \star & \star \\
\star & \star & \star & \star \\
\star & \star & \star & \star
\end{array}\right)
&
\left(\begin{array}{cccc}
\boxed{1} & \star & \star & \star \\
\downarrow & \star & \star & \star \\
\downarrow & \star & \star & \star \\
\downarrow & \star & \star & \star
\end{array}\right)
&
\left(\begin{array}{cccc}
1 & \star & \star & \star \\
0 & \boxed{1} & \star & \star \\
0 & \star & \star & \star \\
0 & \star & \star & \star
\end{array}\right)
\\ \\
\text{\color{blue}Clear down} & \text{\color{blue}(maybe these are already zero)} & \text{\color{blue}Get a 1 here} \\
\left(\begin{array}{cccc}
1 & \star & \star & \star \\
0 & \boxed{1} & \star & \star \\
0 & \downarrow & \star & \star \\
0 & \downarrow & \star & \star
\end{array}\right)
&
\left(\begin{array}{cccc}
1 & \star & \star & \star \\
0 & 1 & \star & \star \\
0 & 0 & \boxed{0} & \star \\
0 & 0 & \boxed{0} & \star
\end{array}\right)
&
\left(\begin{array}{cccc}
1 & \star & \star & \star \\
0 & 1 & \star & \star \\
0 & 0 & 0 & \boxed{\star} \\
0 & 0 & 0 & \star
\end{array}\right)
\\ \\
\text{\color{blue}Clear down} & \text{\color{blue}Matrix is in REF} & \text{\color{blue}Clear up} \\
\left(\begin{array}{cccc}
1 & \star & \star & \star \\
0 & 1 & \star & \star \\
0 & 0 & 0 & \boxed{1} \\
0 & 0 & 0 & \downarrow
\end{array}\right)
&
\left(\begin{array}{cccc}
1 & \star & \star & \star \\
0 & 1 & \star & \star \\
0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0
\end{array}\right)
&
\left(\begin{array}{cccc}
1 & \star & \star & \uparrow \\
0 & 1 & \star & \uparrow \\
0 & 0 & 0 & \boxed{1} \\
0 & 0 & 0 & 0
\end{array}\right)
\\ \\
\text{\color{blue}Clear up} & \text{\color{blue}Matrix is in RREF} & \\
\left(\begin{array}{cccc}
1 & \uparrow & \star & 0 \\
0 & \boxed{1} & \star & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0
\end{array}\right)
&
\left(\begin{array}{cccc}
1 & 0 & \star & 0 \\
0 & 1 & \star & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0
\end{array}\right)
&
\end{array}
$$

### 1.3 Parametric Form 参数形式

#### Objectives 目标
1. Learn to express the solution set of a system of linear equations in parametric form.
2. Understand the three possibilities for the number of solutions of a system of linear equations.
3. Recipe 配方：Parametric Form.
4. Vocabulary word: **_free variable_** 自由变量.

#### Free Variables

**Example**
$$
\begin{cases}
\begin{aligned}
2x + y + 12z &= 1 \\
x + 2y + 9z &= -1
\end{aligned}
\end{cases}
$$

We solve it using row reduction:
\[
\left(
\begin{array}{ccc|c}
2 & 1 & 12 & 1\\
1 & 2 & 9  & -1
\end{array}
\right)
\ \xrightarrow{R_1 \leftrightarrow R_2}\
\left(
\begin{array}{ccc|c}
1 & 2 & 9  & -1\\
2 & 1 & 12 & 1
\end{array}
\right)
\]

\[
\xrightarrow{R_2 = R_2 - 2R_1}\
\left(
\begin{array}{ccc|c}
1 & 2 & 9  & -1\\
0 & -3 & -6 & 3
\end{array}
\right)
\]

\[
\xrightarrow{R_2 = R_2 \div (-3)}\
\left(
\begin{array}{ccc|c}
1 & 2 & 9  & -1\\
0 & 1 & 2  & -1
\end{array}
\right)
\]

\[
\xrightarrow{R_1 = R_1 - 2R_2}\
\left(
\begin{array}{ccc|c}
1 & 0 & 5 & 1\\
0 & 1 & 2 & -1
\end{array}
\right)
\]

This row reduced matrix corresponds to 对应于 the linear system：
$$
\begin{cases}
\begin{aligned}
x + 5z &= 1 \\
y + 2z &= -1
\end{aligned}
\end{cases}
$$

We rewrite as:
$$
\begin{cases}
\begin{aligned}
x &= 1 - 5z \\
y &= -1 - 2z
\end{aligned}
\end{cases}
$$

We have found all solutions: it is the set of all values x,y,z, where
$$
\begin{cases}
\begin{aligned}
x &= 1 - 5z \\
y &= -1 - 2z \\
z &= z
\end{aligned}
\end{cases}
\qquad \text{z any real number}
$$

This is called the parametric form for the solution to the linear system. The variable $z$ is called a free variable.

**Definition**:Consider a consistent system of equations in the variables $x_1$,$x_2$,...,$x_n$.Let $A$ be a row echelon form of the augmented martrix for this system.
We say that $x_1$ is a free variable if its corresponding column in $A$ is not a pivot column 主元列（A pivot column of a matrix is a column that contains a pivot position.）.

#### Recipe: Parametric form
The parametric form of the solution set of a consistent system of linear equations is obtained as follows.
1. Write the system as an augmented matrix.
2. Row reduce to reduced row echelon form.
3. Write the corresponding (solved) system of linear equations.
4. Move all free variables to the right hand side of the equations.

#### Implicit Versus Parameterized Equations The solution set of the system of linear equations 隐式方程与参数化方程；线性方程组的解集
$$
\begin{cases}
\begin{aligned}
2x + y + 12z &= 1 \\
x + 2y + 9z &= -1
\end{aligned}
\end{cases}
$$
is a line in $R^3$, as we saw in this . These equations are called the implicit equations for the line: the line is defined implicitly as the simultaneous solutions to those two equations.
The parametric form  参数形式
$$
\begin{cases}
\begin{aligned}
x &= 1 - 5z \\
x &= -1 - 2z.
\end{aligned}
\end{cases}
$$
can be written as follows:
$$
(x, y, z) = (1 - 5z, -1 - 2z, z) \qquad z \text{ any real number.}
$$
This called a parameterized equation for the same line. It is an expression that produces all points of the line in terms of one parameter, 
$z$.

One should think of a system of equations as being an implicit equation for its solution set, and of the parametric form as being the parameterized equation for the same set. The parameteric form is much more explicit: it gives a concrete recipe for producing all solutions.

#### Number of Solutions  解的数量
There are three possibilities for the reduced row echelon form of the augmented matrix of a linear system.线性方程组的增广矩阵的简化行阶梯形有三种可能性。
1. **The last column is a pivot column.** In this case, the system is inconsistent. There are zero solutions, i.e., the solution set is empty. For example, the matrix
$$
\left(
\begin{array}{cc|c}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}
\right)
$$
comes from a linear system with no solutions.
2. **Every column except the last column is a pivot column.** In this case, the system has a unique solution. For example, the matrix
$$
\left(
\begin{array}{ccc|c}
1 & 0 & 0 & a \\
0 & 1 & 0 & b \\
0 & 0 & 1 & c
\end{array}
\right)
$$
tells us that the unique solution is $(x,y,z) = (a,b,c)$.
3. **The last column is not a pivot column, and some other column is not a pivot column either.** In this case, the system has infinitely many solutions, corresponding to the infinitely many possible values of the free variable(s). For example, in the system corresponding to the matrix
$$
\left(
\begin{array}{cccc|c}
1 & -2 & 0 & 3 & 1 \\
0 & 0 & 1 & 4 & -1
\end{array}
\right)
$$
any values for $x_2$ and $x_4$ yield a solution to the system of equations.