# Python Programming Challenges

## Challenges

### 1. Number Utils - `is_prime_list()`

**รายละเอียดโจทย์:**
ตรวจสอบว่าทุกตัวเลขในรายการเป็นจำนวนเฉพาะหรือไม่

**ตัวอย่าง:**

```python
is_prime_list([1, 2, 3])  # True
is_prime_list([4, 5, 6])  # False (4 และ 6 ไม่ใช่จำนวนเฉพาะ)
```

**วิธีทดสอบ:**

```bash
python -m unittest tests.test_number_utils
```

---

### 2. Cat and Mouse - `cat_and_mouse()`

**รายละเอียดโจทย์:**
แมว 2 ตัว (Cat A และ Cat B) และหนู 1 ตัว (Mouse C) อยู่บนเส้นจำนวนเต็ม ต้องหาว่าแมวตัวไหนจะได้กินหนู

**ตัวอย่าง:**

```python
cat_and_mouse(1, 2, 3)  # "Cat B" (ระยะ: A=2, B=1)
cat_and_mouse(1, 3, 2)  # "Mouse C" (ระยะ: A=1, B=1 เท่ากัน)
```

**วิธีทดสอบ:**

```bash
python -m unittest tests.test_cat_and_mouse
```

---

### 3. Funny String - `funnyString()`

**รายละเอียดโจทย์:**
ตรวจสอบว่าสตริง "ตลก" (Funny) หรือไม่ โดยเปรียบเทียบค่าความแตกต่างของ ASCII ระหว่างตัวอักษรที่ติดกันในสตริงเดิมและสตริงย้อนหลัง

**ตัวอย่าง:**

```python
funnyString("acxz")   # "Funny" (ความแตกต่าง: [2, 21, 2] เท่ากัน)
funnyString("bcxz")   # "Not Funny" (ความแตกต่างไม่เท่ากัน)
```

**วิธีทดสอบ:**

```bash
nose2 -v --with-coverage tests.test_funny_str
```

---

### 4. Alternating Characters - `alternatingCharacters()`

**รายละเอียดโจทย์:**
นับจำนวนตัวอักขระที่ต้องลบออกเพื่อให้สตริงไม่มีตัวอักขระเดียวกันติดกัน 2 ตัว

**ตัวอย่าง:**

```python
alternatingCharacters("AAAA")      # 3 (ลบ A 3 ตัว)
alternatingCharacters("ABABABAB")  # 0 (ไม่ต้องลบ)
alternatingCharacters("AAABBB")     # 4 (ลบ A 2 ตัว, B 2 ตัว)
```

**วิธีทดสอบ:**

```bash
nose2 -v --with-coverage tests.test_alternating_chr
```

---

### 5. Caesar Cipher - `caesarCipher()`

**รายละเอียดโจทย์:**
เข้ารหัสสตริงด้วยวิธี Caesar Cipher โดยเลื่อนตัวอักษรไปทางขวา k ตำแหน่ง

**ตัวอย่าง:**

```python
caesarCipher("abc", 2)    # "cde" (a→c, b→d, c→e)
caesarCipher("xyz", 3)    # "aaa" (x→a, y→a, z→a)
```

**วิธีทดสอบ:**

```bash
nose2 -v --with-coverage tests.test_caesar_cipher
```

---

### 6. Alternate - `alternate()`

**รายละเอียดโจทย์:**
หาความยาวสูงสุดของสตริงย่อยที่เกิดจาก 2 ประเภทตัวอักขระ และสลับกันเรียงไม่ซ้ำกัน

**ตัวอย่าง:**

```python
alternate("beabeefeab")  # 5 (ใช้ b และ a: "babab")
alternate("ababab")      # 6 (ใช้ a และ b: "ababab")
alternate("aaaa")        # 0 (ไม่สามารถสลับกันได้)
```

**วิธีทดสอบ:**

```bash
nose2 -v --with-coverage tests.test_altenate
```

---

### 7. Grid Challenge - `gridChallenge()`

**รายละเอียดโจทย์:**
ตรวจสอบว่าเมื่อเรียงตัวอักษรในแต่ละแถวจากน้อยไปมาก แล้วคอลัมน์ทุกคอลัมน์จะเรียงลำดับจากบนลงล่างหรือไม่

**ตัวอย่าง:**

```python
gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv'])
# "YES" (หลังเรียงแถว: ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxyz'])

gridChallenge(['abc', 'wxy', 'zab'])
# "NO" (คอลัมน์ที่ 2: b > a)
```

**วิธีทดสอบ:**

```bash
nose2 -v --with-coverage tests.test_grid_challenge
```

---

## Author

นาย ธนพิพัฒน์ จันทร์สุวรรณ์ (6810110135)
