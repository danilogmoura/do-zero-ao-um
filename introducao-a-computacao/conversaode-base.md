## Exercícios

---

### 1. Converta para decimal

---

#### a) 0xF0CA

- **Hexadecimal > Binário**

```
F = 15			        0 = 0   	C = 12                  	A = 10
15 / 2 = 7  Resto 1		0		12 / 2 = 6	Resto 0		10 / 2 = 5	Resto 0
7  / 2 = 3  Resto 1		0		6  / 2 = 3	Resto 0		5  / 2 = 2	Resto 1
3  / 2 = 1  Resto 1		0		3  / 2 = 1	Resto 1		2  / 2 = 1  	Resto 0
1  / 2 = 0  Resto 1		0		1  / 2 = 0	Resto 1		1  / 2 = 0	Resto 1
               1111     	0000           			1100                    	1010

= 1111 0000 1100 1010
```

- **Binário > Decimal**

```
= 1111 0000 1100 1010
= 2^15 + 2^14 + 2^13 + 2^12 + 0 + 0 + 0 + 0 + 2^7 + 2^6 + 0 + 0 + 2^3 + 0 + 2^1 + 0
= 32768 + 16384 + 8192 + 4096 + 128 + 64 + 8 + 2
= 61642
```

- **Resposta**: 0xF0CA equivale a 61642

---

#### b) 0b11111111

- **Binário > Decimal**

```
= 1111 1111
= 2^7 +2^6 +2^5 +2^4 +2^3 +2^2 +2^1 +2^0 
= 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1
= 255
```
- **Resposta**: 0b11111111 equivale a 255

---

#### c) 0x1A

- **Hexadecimal > Binário**

```
1 = 1				A = 10
---------	-------		10 / 2 = 5	Resto 0
---------	-------		5  / 2 = 2	Resto 1
---------	-------		2  / 2 = 1	Resto 0
1 / 2 = 0	Resto 1		1  / 2 = 0	Resto 1
		0001				1010
= 0001 1010
```

- **Binário > Decimal**

```
= 0 + 0 + 0 + 2^4 + 2^3 + 0 + 2^1 + 0 
= 16 + 8 + 2
= 26
```

- **Resposta**: 0x1A equivale a 26

---

#### d) 0b1010

- **Binário > Decimal**

```
= 1010
= 2^3 + 0 + 2^1 + 0
= 8 + 2
= 10
```

- **Resposta**: 0b1010 equivale a 10

---

### 2. Converta para hexadecimal

---

#### a) 2024

- **Decimal > Binário**

```
= 2024 / 2 = 1012	Resto 0
= 1012 / 2 =  506	Resto 0
=  506 / 2 =  253	Resto 0
=  253 / 2 =  126	Resto 1
=  126 / 2 =   63   	Resto 0
=   63 / 2 =   31	Resto 1
=   31 / 2 =   15   	Resto 1
=   15 / 2 =    7   	Resto 1
=    7 / 2 =    3   	Resto 1
=    3 / 2 =    1	Resto 1
=    1 / 2 = 	0	Resto 1

= 0x0111 1110 1000
```

- **Binário > Hexadecimal**

```
0111                    1110				        1000
= 2^2 + 2^1 + 2^0	= 2^3 + 2^2 + 2^1 + 0			= 2^3
= 4 + 2 + 1             = 8 + 4 + 2			        = 8
= 7                     = E

= 7E8
```

- **Resposta**: 2024 equivale a 0x7E8

---

#### b) 0b111

- **Binário > Hexadecimal**

```
= 0111
= 2^2 + 2^1 + 2^0
= 4 + 2 + 1 
= 7
```

- **Resposta**: 0b111 equivale a 0x7

---

#### c) 0b1011

- **Binário > Hexadecimal**

```
= 2^3 + 0 + 2^1 + 2^0
= 8 + 0 + 2 + 1
= B
```

- **Resposta**: 0b1011 equivale a 0xB

---

### 3. Quem é maior?

---

#### a) 0xf0 ou 0xff?

- **0xFF**: valor máximo de 1 byte, equivale a 255

- **Resposta**: 0xFF

---

#### b) 0xD ou 12?

- **0xD** equivale a 13

- **Resposta**: 0xD

---

#### c) 0b1111 ou 0xe?

- **0b1111** equivale a 15  
- **0xE** equivale a 14  

- **Resposta**: 0b1111
