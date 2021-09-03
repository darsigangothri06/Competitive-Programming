A lockdown has been put in place due to the pandemic.

You cannot step out to buy food, however you can have food delivered to you.

You can purchase any amount of food in one delivery.

There is a constant delivery fee for every delivery, regardless of the amount of food purchased in the delivery.

Each type of food on the menu has two properties: a price per meal and freshness-time

One "meal" of food will feed you for one day; once a meal has been eaten, it cannot be eaten again.

The freshness-time of a type of food is the maximum number of days for which that food can still be eaten, counting from when you received it.

```
A freshness-time of zero means you must eat that type of food on the day of delivery.
In a single delivery you can purchase as many different types of food, and as many meals of each of those types, as you have money for.
```

The food will be delivered on the same day that you purchased it, and you will eat one of the food on the same day.

Food delivery is the only way for you to receive food.

Given an amount of money, which you can spend on meal prices and delivery fees,

```
what is the maximum number of days for which you cn eat food every day - 
counting from the day which you order?
```

#### Input

```
Each test case will begin with three integers, A, B and C, denoting the amount of money you have, the delivery fee, and the number of types of food provided by the restaurant, respectively.

C lines follow, each will consist of two integers, Pi and Fi,  denoting respectively the price-per-meal and freshness-time of one type of food
```



#### Output

```
Number of days you will eat food
```



##### Sample Input/Output

```
Input:
32 5 2
5 0
10 2

Output:
3
```

