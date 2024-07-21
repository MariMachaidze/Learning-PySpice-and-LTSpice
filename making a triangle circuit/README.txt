Prompt:
 - We have the resistors connected to each other like a triangle with A, B, C points. known as delta network
 - Every resistor is different from each other. 
 - AB point is powered. 
 - We are looking for how current in BC is dependent on R3 (AC points).

Solution:

 AB points - R1 - i1 - v1
 BC points - R2 - i2 - v2
 AC points - R3 - i3 - v3

 We are looking for i2/R3

 when we create a circuit we get that R2 and R3 are in series and together they are in parallel with R1.
 From Electrical Engineering we know that in parallel connection voltages are same and in series connection current is same.
 We get that i2 = i3 meaning we are looking for i3/R3 = v3
 v1 = v2 + v3 = v
 we can find v3 with voltage divider formula v3 = v * R3 / (R2 + R3)