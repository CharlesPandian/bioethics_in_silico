"""
Generate 100 authentic Grade 4-5 math word and procedural problems
Stratified equally across 4 domains (25 items each):
1. Multi-Step Arithmetic Word Problems (ARITH)
2. Fractions & Decimals (FRAC)
3. Ratios & Proportions (RATIO)
4. Introductory Geometry & Measurement (GEOM)

Each item includes:
- item_id
- domain
- grade_level
- knowledge_component
- problem_text
- target_answer
- solution_steps
- distractor_d1 (conceptual/developmental misconception)
- distractor_d2 (procedural/calculation slip)
"""

import json
import csv
from pathlib import Path

def create_benchmark_items():
    items = []
    
    # -------------------------------------------------------------
    # Domain 1: Multi-Step Arithmetic Word Problems (25 items: 1-25)
    # -------------------------------------------------------------
    arith_specs = [
        ("Maya had $45. She bought 3 books that cost $8 each and a notebook for $5. How much money does she have left?",
         "16", "$16",
         "1. Calculate total book cost: 3 * 8 = 24. 2. Add notebook: 24 + 5 = 29. 3. Subtract from original money: 45 - 29 = 16.",
         "21", "Maya forgot to subtract notebook: 45 - 24 = 21",
         "29", "Student computed total spent ($29) instead of money left"),
         
        ("A school cafeteria ordered 8 boxes of apples with 24 apples in each box. If 135 apples were eaten at lunch, how many apples remain?",
         "57", "57 apples",
         "1. Total apples: 8 * 24 = 192. 2. Remaining apples: 192 - 135 = 57.",
         "168", "Student subtracted 24 - 8 or made arithmetic slip on subtraction: 192 - 135 = 168",
         "192", "Student calculated total apples (192) but omitted the subtraction step"),
         
        ("Leo saved $12 each week for 6 weeks. Then his grandmother gave him $25 for his birthday. If he buys a skateboard for $70, how much money does he have left?",
         "27", "$27",
         "1. Savings: 12 * 6 = 72. 2. Add gift: 72 + 25 = 97. 3. Subtract skateboard: 97 - 70 = 27.",
         "2", "Student subtracted skateboard from savings only: 72 - 70 = 2, forgetting gift",
         "97", "Student calculated total saved ($97) without deducting skateboard cost"),
         
        ("A baker baked 144 cookies. She packed them equally into 12 gift boxes. If she sold 9 gift boxes, how many cookies did she sell?",
         "108", "108 cookies",
         "1. Cookies per box: 144 / 12 = 12. 2. Cookies sold: 12 * 9 = 108.",
         "36", "Student calculated remaining cookies (12 * 3 = 36) instead of sold cookies",
         "21", "Student added boxes: 12 + 9 = 21"),
         
        ("A toy factory produces 45 teddy bears every hour. The factory runs for 7 hours a day. On Friday, 30 teddy bears were found defective and discarded. How many good bears were produced?",
         "285", "285 teddy bears",
         "1. Total produced: 45 * 7 = 315. 2. Good bears: 315 - 30 = 285.",
         "315", "Student omitted subtraction of defective bears",
         "345", "Student added defective bears: 315 + 30 = 345"),
         
        ("Ethan has 5 packs of baseball cards with 14 cards in each pack. His brother gave him 18 more cards. Ethan then gave 25 cards to his best friend. How many cards does Ethan have now?",
         "63", "63 cards",
         "1. Initial cards: 5 * 14 = 70. 2. Total after gift: 70 + 18 = 88. 3. Remaining: 88 - 25 = 63.",
         "88", "Student forgot to subtract cards given away",
         "45", "Student subtracted 25 from 70 = 45 without adding brother's cards"),
         
        ("A movie theater has 15 rows of seats with 18 seats in each row. For the afternoon showing, 195 seats were occupied. How many seats were empty?",
         "75", "75 seats",
         "1. Total seats: 15 * 18 = 270. 2. Empty seats: 270 - 195 = 75.",
         "270", "Student gave total capacity instead of empty seats",
         "85", "Subtraction regrouping error: 270 - 195 = 85"),
         
        ("A farmer collected 210 eggs from her hens. She put 12 eggs in each carton. How many full cartons can she pack, and how many eggs will be left over?",
         "17 cartons and 6 eggs", "17 cartons, 6 eggs",
         "1. 210 / 12 = 17 with remainder 6 (17 * 12 = 204; 210 - 204 = 6).",
         "17.5 cartons", "Student expressed remainder as a decimal without identifying discrete eggs",
         "18 cartons", "Student rounded up without accounting for left-over eggs"),
         
        ("Priya bought 4 shirts for $15 each and 2 pairs of jeans for $28 each. She paid with two $100 bills. How much change did she receive?",
         "84", "$84",
         "1. Shirts: 4 * 15 = 60. 2. Jeans: 2 * 28 = 56. 3. Total spent: 60 + 56 = 116. 4. Cash: 2 * 100 = 200. 5. Change: 200 - 116 = 84.",
         "116", "Student reported total spent ($116) instead of change",
         "-16", "Student subtracted total spent from a single $100 bill: 100 - 116"),
         
        ("A school bus travels 28 miles on Monday morning and 32 miles in the afternoon. It repeats this route for 5 school days. What is the total mileage for the week?",
         "300", "300 miles",
         "1. Daily mileage: 28 + 32 = 60 miles. 2. Weekly total: 60 * 5 = 300 miles.",
         "172", "Student multiplied only one route: 28 + (32 * 5) = 188 or 28*5 + 32 = 172",
         "60", "Student found daily total but did not multiply by 5"),
         
        ("A library has 3 shelves of fiction books with 35 books per shelf, and 4 shelves of science books with 28 books per shelf. How many books are there in total?",
         "217", "217 books",
         "1. Fiction: 3 * 35 = 105. 2. Science: 4 * 28 = 112. 3. Total: 105 + 112 = 217.",
         "63", "Student added books per shelf: 35 + 28 = 63",
         "196", "Student multiplied (3+4) * 28 = 196"),
         
        ("Marcus earns $9 per hour mowing lawns. Last week he worked 14 hours. He spent $42 on lawn mower gas and tune-up. How much profit did he make?",
         "84", "$84",
         "1. Total revenue: 9 * 14 = 126. 2. Profit: 126 - 42 = 84.",
         "126", "Student calculated gross revenue without subtracting expenses",
         "168", "Student added expenses to earnings: 126 + 42 = 168"),
         
        ("An art teacher has 250 sheets of colored construction paper. She gives 6 sheets to each of her 32 students. How many sheets of paper does she have left?",
         "58", "58 sheets",
         "1. Distributed: 32 * 6 = 192. 2. Left over: 250 - 192 = 58.",
         "192", "Student reported sheets distributed instead of leftover",
         "68", "Regrouping subtraction slip: 250 - 192 = 68"),
         
        ("A freight train has 6 grain cars holding 48 tons each and 8 coal cars holding 55 tons each. What is the total weight of the cargo in tons?",
         "728", "728 tons",
         "1. Grain: 6 * 48 = 288 tons. 2. Coal: 8 * 55 = 440 tons. 3. Total: 288 + 440 = 728 tons.",
         "103", "Student added cargo per car: 48 + 55 = 103",
         "700", "Multiplication approximation slip"),
         
        ("Sophia bought 6 packs of stickers with 15 stickers each. She kept 20 stickers for herself and divided the rest equally among 5 friends. How many stickers did each friend receive?",
         "14", "14 stickers",
         "1. Total stickers: 6 * 15 = 90. 2. Remaining to share: 90 - 20 = 70. 3. Per friend: 70 / 5 = 14.",
         "18", "Student divided total without subtracting Sophia's stickers: 90 / 5 = 18",
         "10", "Subtracted 20 / 5 = 4; 14 slips to 10"),
         
        ("A sports store received 12 crates of basketballs. Each crate has 16 balls. The store sold 68 balls during a weekend tournament. How many basketballs are left?",
         "124", "124 basketballs",
         "1. Total balls: 12 * 16 = 192. 2. Remaining: 192 - 68 = 124.",
         "192", "Total received without subtracting sales",
         "134", "Subtraction borrowing error: 192 - 68 = 134"),
         
        ("Chloe had 180 beads. She used 45 beads to make a necklace and 15 beads for each of 4 bracelets. How many beads does Chloe have left?",
         "75", "75 beads",
         "1. Necklace: 45. 2. Bracelets: 4 * 15 = 60. 3. Total used: 45 + 60 = 105. 4. Remaining: 180 - 105 = 75.",
         "120", "Subtracted only bracelets: 180 - 60 = 120",
         "135", "Subtracted only necklace: 180 - 45 = 135"),
         
        ("A community garden has 8 plots. Each plot has 14 tomato plants and 6 pepper plants. What is the total number of plants in all plots?",
         "160", "160 plants",
         "1. Plants per plot: 14 + 6 = 20. 2. Total plants: 8 * 20 = 160.",
         "112", "Counted only tomato plants: 8 * 14 = 112",
         "48", "Counted only pepper plants: 8 * 6 = 48"),
         
        ("Jackson bought 3 sandwiches for $7 each and 3 juice bottles for $2 each. If he pays with a $50 bill, how much change should he receive?",
         "23", "$23",
         "1. Sandwiches: 3 * 7 = 21. 2. Juices: 3 * 2 = 6. 3. Total spent: 21 + 6 = 27. 4. Change: 50 - 27 = 23.",
         "27", "Student gave total spent ($27) instead of change",
         "33", "Student subtracted only sandwiches: 50 - 21 = 29 or arithmetic slip 33"),
         
        ("A shipping crate can carry 75 pounds. Workers placed 4 packages weighing 12 pounds each and 2 packages weighing 9 pounds each inside. How many more pounds can the crate hold?",
         "9", "9 pounds",
         "1. 4 * 12 = 48 lbs. 2. 2 * 9 = 18 lbs. 3. Total weight: 48 + 18 = 66 lbs. 4. Remaining capacity: 75 - 66 = 9 lbs.",
         "66", "Total current weight without subtracting from capacity",
         "15", "Subtracted only 48 from 75 = 27; slip to 15"),
         
        ("A classroom has 24 student desks. The teacher puts 5 pencils and 2 erasers on each desk. How many items (pencils and erasers combined) were placed on the desks?",
         "168", "168 items",
         "1. Items per desk: 5 + 2 = 7. 2. Total items: 24 * 7 = 168.",
         "120", "Calculated pencils only: 24 * 5 = 120",
         "48", "Calculated erasers only: 24 * 2 = 48"),
         
        ("Liam had 350 points in a video game. He scored 45 points in round one and doubled his total score in round two. How many points does he have now?",
         "790", "790 points",
         "1. Round 1 score: 350 + 45 = 395. 2. Doubled: 395 * 2 = 790.",
         "440", "Doubled only the round 1 addition: 350 + (45 * 2) = 440",
         "700", "Doubled only initial score: 350 * 2 = 700"),
         
        ("A concert hall has 400 tickets. It sells 145 adult tickets at $10 and 180 child tickets at $6. How many tickets were left unsold?",
         "75", "75 tickets",
         "1. Tickets sold: 145 + 180 = 325. 2. Unsold: 400 - 325 = 75.",
         "2530", "Student calculated dollar revenue instead of ticket count",
         "325", "Reported tickets sold rather than unsold"),
         
        ("Emma baked 5 trays of muffins with 12 muffins on each tray. She gave 18 muffins to her neighbors and packaged the rest into bags of 6. How many bags did she make?",
         "7", "7 bags",
         "1. Total muffins: 5 * 12 = 60. 2. After neighbors: 60 - 18 = 42. 3. Bags: 42 / 6 = 7.",
         "10", "Divided total muffins without subtracting neighbor gift: 60 / 6 = 10",
         "42", "Reported muffins remaining to package instead of bag count"),
         
        ("A delivery driver has 95 packages. In the morning, he delivers 42 packages. In the afternoon, he delivers 28 packages. In the evening, his warehouse gives him 15 new packages. How many packages are in his truck now?",
         "40", "40 packages",
         "1. Total delivered: 42 + 28 = 70. 2. Remaining before evening: 95 - 70 = 25. 3. Add evening packages: 25 + 15 = 40.",
         "25", "Forgot to add the new evening packages: 95 - 70 = 25",
         "110", "Added delivered packages instead of subtracting: 95 + 70 - 15")
    ]
    
    for i, spec in enumerate(arith_specs, start=1):
        items.append({
            "item_id": f"MATH_G5_{i:03d}",
            "domain": "Multi-Step Arithmetic Word Problems",
            "domain_code": "ARITH",
            "grade_level": "Grade 5",
            "knowledge_component": "multi_step_arithmetic_operations",
            "problem_text": spec[0],
            "target_answer": spec[1],
            "display_answer": spec[2],
            "solution_steps": spec[3],
            "distractor_d1": spec[4],
            "distractor_d1_reason": spec[5],
            "distractor_d2": spec[6],
            "distractor_d2_reason": spec[7]
        })
        
    # -------------------------------------------------------------
    # Domain 2: Fractions & Decimals (25 items: 26-50)
    # -------------------------------------------------------------
    frac_specs = [
        ("What is 1/3 + 1/4? Write your answer as a simplified fraction.",
         "7/12", "7/12",
         "1. Find common denominator for 3 and 4, which is 12. 2. Convert: 1/3 = 4/12, 1/4 = 3/12. 3. Add numerators: 4/12 + 3/12 = 7/12.",
         "2/7", "Child added numerators and denominators directly: (1+1)/(3+4) = 2/7",
         "1/12", "Subtracted numerators or multiplied denominators: 1/12"),
         
        ("Calculate 5/6 - 2/3. Express your answer as a simplified fraction.",
         "1/6", "1/6",
         "1. Find common denominator: 6. 2. Convert 2/3 = 4/6. 3. Subtract numerators: 5/6 - 4/6 = 1/6.",
         "3/3", "Child subtracted across numerators and denominators: (5-2)/(6-3) = 3/3 = 1",
         "3/6", "Subtracted without converting denominator: 5/6 - 2/6 = 3/6"),
         
        ("A recipe calls for 3/4 cup of sugar. Noah wants to make 1/2 of the recipe. How much sugar should he use?",
         "3/8", "3/8 cup",
         "1. Multiply fractions: 3/4 * 1/2 = (3*1)/(4*2) = 3/8 cup.",
         "2/4", "Subtracted fractions: 3/4 - 1/2 = 1/4 or 2/4",
         "4/6", "Added numerators and denominators: (3+1)/(4+2) = 4/6"),
         
        ("What is 2 and 1/2 + 1 and 3/4? Express as a mixed number or improper fraction in simplest form.",
         "4 1/4", "4 1/4 (or 17/4)",
         "1. Add whole numbers: 2 + 1 = 3. 2. Add fractions: 1/2 + 3/4 = 2/4 + 3/4 = 5/4 = 1 1/4. 3. Combine: 3 + 1 1/4 = 4 1/4.",
         "3 4/6", "Added whole numbers and fractions across: 3 and (1+3)/(2+4) = 3 4/6",
         "3 3/4", "Omitted the 1/2 fraction conversion"),
         
        ("Convert 0.75 into a fraction in simplest form.",
         "3/4", "3/4",
         "1. 0.75 means 75 hundredths = 75/100. 2. Divide numerator and denominator by 25: 75/25 = 3, 100/25 = 4. Result: 3/4.",
         "75/10", "Misidentified place value as tenths instead of hundredths",
         "7/5", "Wrote digits as fraction 7/5"),
         
        ("What is 4.35 + 2.8? Express your answer as a decimal.",
         "7.15", "7.15",
         "1. Line up decimal points: 4.35 + 2.80. 2. Add hundredths: 5 + 0 = 5. 3. Add tenths: 3 + 8 = 11 (write 1, carry 1). 4. Add whole: 4 + 2 + 1 = 7. Result: 7.15.",
         "6.43", "Aligned numbers from right without aligning decimal: 4.35 + 0.28 = 4.63 or 4.35 + 2.8 = 6.43",
         "7.13", "Arithmetic addition slip in tenths"),
         
        ("Evaluate: 8.5 - 3.75.",
         "4.75", "4.75",
         "1. Pad with zero: 8.50 - 3.75. 2. Regroup from whole: 8.50 -> 7 and 1.50 -> 7 and 14 tenths and 10 hundredths. 10 - 5 = 5; 14 - 7 = 7; 7 - 3 = 4. Result: 4.75.",
         "5.25", "Subtracted smaller from larger digit without borrowing: 5 - 0 = 5, 7 - 5 = 2, 8 - 3 = 5 -> 5.25",
         "4.25", "Failed to regroup tenths after borrowing hundredths"),
         
        ("What is 3/5 of 45?",
         "27", "27",
         "1. Divide 45 by denominator 5: 45 / 5 = 9. 2. Multiply by numerator 3: 9 * 3 = 27.",
         "15", "Computed 1/3 of 45 or divided 45 by 3",
         "75", "Multiplied 45 * 5 / 3 = 75"),
         
        ("Order these decimals from least to greatest: 0.4, 0.25, 0.305.",
         "0.25, 0.305, 0.4", "0.25, 0.305, 0.4",
         "1. Compare tenths place: 0.25 has 2 tenths, 0.305 has 3 tenths, 0.400 has 4 tenths. 2. Ascending order: 0.25 < 0.305 < 0.4.",
         "0.4, 0.25, 0.305", "Longer number is bigger misconception: 4 is shortest so smallest, 305 is longest so biggest",
         "0.305, 0.25, 0.4", "Misordered tenths"),
         
        ("A rope is 6 meters long. A worker cuts off pieces that are each 3/4 meter long. How many pieces can be cut?",
         "8", "8 pieces",
         "1. Divide 6 by 3/4: 6 / (3/4) = 6 * (4/3) = 24 / 3 = 8 pieces.",
         "4.5", "Multiplied instead of dividing: 6 * 3/4 = 4.5",
         "18", "Multiplied 6 * 3 = 18"),
         
        ("Add: 3/8 + 1/2. Write the answer in simplest form.",
         "7/8", "7/8",
         "1. Common denominator: 8. 2. 1/2 = 4/8. 3. 3/8 + 4/8 = 7/8.",
         "4/10", "Added across: (3+1)/(8+2) = 4/10 = 2/5",
         "5/8", "Added 1 without converting: 3/8 + 1/8 = 4/8 or slip 5/8"),
         
        ("What is 0.6 * 0.4?",
         "0.24", "0.24",
         "1. Multiply whole numbers: 6 * 4 = 24. 2. Count decimal places: 1 + 1 = 2 places. Result: 0.24.",
         "2.4", "Lost decimal place: placed only one decimal digit",
         "0.024", "Excess decimal shift"),
         
        ("Subtract: 1 - 5/12. Express as a simplified fraction.",
         "7/12", "7/12",
         "1. Express 1 as 12/12. 2. 12/12 - 5/12 = 7/12.",
         "4/12", "Subtracted 5 - 1 = 4 -> 4/12",
         "5/11", "Subtracted 1 from denominator: 5/(12-1) = 5/11"),
         
        ("Which fraction is larger: 3/5 or 5/8?",
         "5/8", "5/8 (5/8 = 0.625 > 3/5 = 0.600)",
         "1. Cross multiply: 3 * 8 = 24 vs 5 * 5 = 25. 2. Since 25 > 24, 5/8 > 3/5.",
         "3/5", "Saw 3 and 5 closer to each other or miscalculated cross product",
         "Equal", "Estimated both around 1/2 and assumed equal"),
         
        ("Calculate: 12.6 / 3.",
         "4.2", "4.2",
         "1. 12 tenths divided by 3 is 4 units; 6 tenths divided by 3 is 2 tenths. 2. 12.6 / 3 = 4.2.",
         "42", "Ignored decimal point",
         "0.42", "Moved decimal point an extra place to left"),
         
        ("Express 3/20 as a decimal.",
         "0.15", "0.15",
         "1. Multiply numerator and denominator by 5: 3*5 / 20*5 = 15/100. 2. 15/100 = 0.15.",
         "0.3", "Assumed 3/20 = 0.3 because numerator is 3",
         "0.015", "Divided by 1000 instead of 100"),
         
        ("Lucas ate 2/5 of a pizza for lunch and 1/3 of the same pizza for dinner. What fraction of the pizza did he eat altogether?",
         "11/15", "11/15",
         "1. Common denominator for 5 and 3 is 15. 2. 2/5 = 6/15, 1/3 = 5/15. 3. 6/15 + 5/15 = 11/15.",
         "3/8", "Added numerators and denominators: (2+1)/(5+3) = 3/8",
         "7/15", "Forgot to multiply numerator of 2/5: 2/15 + 5/15 = 7/15"),
         
        ("Evaluate: 4 * (2/3). Write as a mixed number.",
         "2 2/3", "2 2/3 (or 8/3)",
         "1. 4 * 2/3 = (4*2)/3 = 8/3. 2. 8/3 = 2 with remainder 2 = 2 2/3.",
         "8/12", "Multiplied both numerator and denominator by 4: (4*2)/(4*3) = 8/12",
         "6/3", "Added whole number to numerator: (4+2)/3 = 6/3 = 2"),
         
        ("What is 15.4 - 9.68?",
         "5.72", "5.72",
         "1. Align: 15.40 - 9.68. 2. Regroup: 10 - 8 = 2; 13 - 6 = 7; 14 - 9 = 5. Result: 5.72.",
         "6.28", "Subtracted smaller digits: 8 - 0 = 8, 6 - 4 = 2, 15 - 9 = 6 -> 6.28",
         "5.82", "Borrowing error in tenths"),
         
        ("Simplify the fraction 24/36 to its lowest terms.",
         "2/3", "2/3",
         "1. Greatest common factor of 24 and 36 is 12. 2. 24 / 12 = 2, 36 / 12 = 3. Result: 2/3.",
         "4/6", "Divided by 6 instead of GCF 12 (not fully simplified)",
         "12/18", "Divided by 2 only"),
         
        ("Find the sum: 0.05 + 0.8 + 0.12.",
         "0.97", "0.97",
         "1. Align decimals: 0.05 + 0.80 + 0.12. 2. Hundredths: 5 + 0 + 2 = 7. 3. Tenths: 0 + 8 + 1 = 9. Result: 0.97.",
         "0.25", "Misaligned 0.8 as 0.08: 0.05 + 0.08 + 0.12 = 0.25",
         "1.07", "Addition carrying error"),
         
        ("What fraction of an hour is 45 minutes? Express in simplest form.",
         "3/4", "3/4 hour",
         "1. An hour has 60 minutes. 2. 45/60. 3. Divide by 15: 45/15 = 3, 60/15 = 4. Result: 3/4.",
         "45/100", "Assumed 100 minutes in an hour",
         "4/5", "Simplified incorrectly"),
         
        ("Calculate: 2/7 + 3/7 + 1/7.",
         "6/7", "6/7",
         "1. Common denominator is 7. 2. Add numerators: 2 + 3 + 1 = 6. Result: 6/7.",
         "6/21", "Added denominators: 7 + 7 + 7 = 21",
         "1", "Assumed 6/7 rounds to 1"),
         
        ("What is 5 divided by 1/4?",
         "20", "20",
         "1. Dividing by a fraction is multiplying by its reciprocal: 5 / (1/4) = 5 * 4 = 20.",
         "5/4", "Multiplied by the fraction: 5 * 1/4 = 5/4 = 1.25",
         "1/20", "Inverted 5: 1/(5*4) = 1/20"),
         
        ("A pitcher contains 1.75 liters of lemonade. Zoe pours 0.6 liters into a glass. How much lemonade is left in the pitcher?",
         "1.15", "1.15 liters",
         "1. Align decimals: 1.75 - 0.60. 2. 1.75 - 0.60 = 1.15 liters.",
         "1.69", "Misaligned 0.6 as 0.06: 1.75 - 0.06 = 1.69",
         "1.11", "Subtracted 6 from 7 and 5: slip 1.11")
    ]
    
    for j, spec in enumerate(frac_specs, start=26):
        items.append({
            "item_id": f"MATH_G5_{j:03d}",
            "domain": "Fractions & Decimals",
            "domain_code": "FRAC",
            "grade_level": "Grade 5",
            "knowledge_component": "fractions_and_decimals_operations",
            "problem_text": spec[0],
            "target_answer": spec[1],
            "display_answer": spec[2],
            "solution_steps": spec[3],
            "distractor_d1": spec[4],
            "distractor_d1_reason": spec[5],
            "distractor_d2": spec[6],
            "distractor_d2_reason": spec[7]
        })
        
    # -------------------------------------------------------------
    # Domain 3: Ratios & Proportions (25 items: 51-75)
    # -------------------------------------------------------------
    ratio_specs = [
        ("The ratio of red marbles to blue marbles in a bag is 2:3. If there are 18 blue marbles, how many red marbles are there?",
         "12", "12 red marbles",
         "1. Ratio is 2:3. 2. Blue marbles = 18. Scale factor = 18 / 3 = 6. 3. Red marbles = 2 * 6 = 12.",
         "17", "Additive reasoning instead of multiplicative: 3 + 15 = 18, so 2 + 15 = 17",
         "27", "Multiplied blue ratio instead of red: 18 * 3 / 2 = 27"),
         
        ("A car travels 150 miles on 5 gallons of gasoline. How many miles does it travel per gallon?",
         "30", "30 miles per gallon",
         "1. Unit rate: 150 miles / 5 gallons = 30 miles per gallon.",
         "750", "Multiplied miles by gallons: 150 * 5 = 750",
         "25", "Division slip: 150 / 5 = 25"),
         
        ("If 4 notebooks cost $6, how much would 10 notebooks cost at the same unit price?",
         "15", "$15",
         "1. Unit price per notebook: $6 / 4 = $1.50. 2. Cost of 10 notebooks: 10 * $1.50 = $15.",
         "12", "Additive reasoning: 4 + 6 = 10, so 6 + 6 = 12",
         "20", "Assumed $2 each: 10 * 2 = 20"),
         
        ("In a fifth-grade class, the ratio of boys to girls is 4:5. If there are 20 girls, how many total students are in the class?",
         "36", "36 students",
         "1. Girls = 20 (corresponding to 5 parts). Scale factor = 20 / 5 = 4. 2. Boys = 4 * 4 = 16. 3. Total students = 16 boys + 20 girls = 36 students.",
         "16", "Reported only the number of boys (16) instead of total students",
         "25", "Additive reasoning: 20 + (5-4) = 21 or slip 25"),
         
        ("A machine stamps 120 bottle caps in 3 minutes. At this rate, how many bottle caps can it stamp in 8 minutes?",
         "320", "320 bottle caps",
         "1. Unit rate: 120 / 3 = 40 caps per minute. 2. In 8 minutes: 40 * 8 = 320 caps.",
         "125", "Additive reasoning: 3 + 5 = 8, so 120 + 5 = 125",
         "240", "Doubled rate: 120 * 2 = 240"),
         
        ("To make orange paint, Ava mixes 3 cups of red paint with 2 cups of yellow paint. If she uses 9 cups of red paint, how many cups of yellow paint does she need?",
         "6", "6 cups",
         "1. Ratio of red to yellow is 3:2. 2. Red paint = 9 cups. Multiplier = 9 / 3 = 3. 3. Yellow paint = 2 * 3 = 6 cups.",
         "8", "Additive thinking: 3 + 6 = 9, so 2 + 6 = 8",
         "13.5", "Cross multiplied backwards: 9 * 3 / 2 = 13.5"),
         
        ("A runner completes 4 laps in 10 minutes. How many minutes will it take her to complete 12 laps at the same pace?",
         "30", "30 minutes",
         "1. Factor of increase: 12 laps / 4 laps = 3. 2. Total time: 10 minutes * 3 = 30 minutes.",
         "18", "Additive reasoning: 4 + 8 = 12, so 10 + 8 = 18",
         "48", "Multiplied 4 * 12 = 48"),
         
        ("A recipe uses 2 eggs for every 3 cups of flour. If a chef uses 12 cups of flour, how many eggs are needed?",
         "8", "8 eggs",
         "1. Flour scale factor = 12 / 3 = 4. 2. Eggs needed = 2 * 4 = 8 eggs.",
         "11", "Additive reasoning: 3 + 9 = 12, so 2 + 9 = 11",
         "18", "Multiplied flour by 3/2 instead: 12 * 3 / 2 = 18"),
         
        ("A scale model of a building uses the scale 1 inch = 15 feet. If the model is 6 inches tall, what is the actual height of the building in feet?",
         "90", "90 feet",
         "1. Scale is 1 inch to 15 feet. 2. Actual height = 6 * 15 = 90 feet.",
         "21", "Added scale values: 15 + 6 = 21",
         "2.5", "Divided instead of multiplying: 15 / 6 = 2.5"),
         
        ("There are 35 students in a choir. The ratio of sopranos to altos is 3:4. How many altos are in the choir?",
         "20", "20 altos",
         "1. Total parts = 3 + 4 = 7 parts. 2. Value per part = 35 / 7 = 5 students. 3. Altos = 4 parts * 5 = 20 altos.",
         "15", "Reported sopranos (3 * 5 = 15) instead of altos",
         "28", "Assumed 4/5 of 35 = 28"),
         
        ("A cyclist travels 36 miles in 3 hours. At this unit rate, how far will the cyclist travel in 5 hours?",
         "60", "60 miles",
         "1. Unit speed = 36 / 3 = 12 miles per hour. 2. Distance in 5 hours = 12 * 5 = 60 miles.",
         "38", "Additive reasoning: 3 + 2 = 5, so 36 + 2 = 38",
         "48", "Calculated for 4 hours: 12 * 4 = 48"),
         
        ("A 12-ounce box of cereal costs $3.60. What is the unit cost per ounce?",
         "0.30", "$0.30 per ounce (or 30 cents)",
         "1. Unit cost = $3.60 / 12 ounces = $0.30 per ounce.",
         "3.33", "Divided ounces by cost: 12 / 3.60 = 3.33",
         "0.03", "Decimal point placement error: 3 cents instead of 30 cents"),
         
        ("The ratio of cats to dogs at an animal shelter is 5:7. If there are 35 cats, how many dogs are at the shelter?",
         "49", "49 dogs",
         "1. Ratio cats:dogs = 5:7. 2. Cats = 35 -> Multiplier = 35 / 5 = 7. 3. Dogs = 7 * 7 = 49 dogs.",
         "37", "Additive reasoning: 5 + 30 = 35, so 7 + 30 = 37",
         "25", "Multiplied cats by 5/7: 35 * 5 / 7 = 25"),
         
        ("A map scale shows that 2 centimeters represents 50 kilometers. What actual distance is represented by 7 centimeters?",
         "175", "175 kilometers",
         "1. 1 cm = 50 / 2 = 25 km. 2. 7 cm = 7 * 25 = 175 km.",
         "55", "Additive reasoning: 2 + 5 = 7, so 50 + 5 = 55",
         "350", "Multiplied 7 * 50 = 350 without dividing by 2"),
         
        ("If 5 packs of juice boxes cost $15, how many packs can you buy with $45?",
         "15", "15 packs",
         "1. Cost per pack = 15 / 5 = $3. 2. Packs for $45 = 45 / 3 = 15 packs (or 45/15 = 3 times 5 = 15).",
         "35", "Additive reasoning: 15 + 30 = 45, so 5 + 30 = 35",
         "9", "Divided 45 / 5 = 9"),
         
        ("A fruit bowl contains apples and bananas in the ratio 4:3. If there are 28 pieces of fruit in total, how many apples are there?",
         "16", "16 apples",
         "1. Total parts = 4 + 3 = 7. 2. Each part = 28 / 7 = 4 pieces. 3. Apples = 4 * 4 = 16.",
         "12", "Reported number of bananas (3 * 4 = 12)",
         "7", "Reported total parts instead of apples"),
         
        ("A faucet drips 15 milliliters of water every 2 minutes. How much water will drip in 10 minutes?",
         "75", "75 milliliters",
         "1. Multiplier for time: 10 / 2 = 5. 2. Water dripped = 15 * 5 = 75 ml.",
         "23", "Additive reasoning: 2 + 8 = 10, so 15 + 8 = 23",
         "150", "Multiplied 15 * 10 = 150 without dividing by 2"),
         
        ("A printer prints 48 pages in 4 minutes. How many pages can it print in 7 minutes?",
         "84", "84 pages",
         "1. Unit rate = 48 / 4 = 12 pages per minute. 2. In 7 minutes = 12 * 7 = 84 pages.",
         "51", "Additive reasoning: 4 + 3 = 7, so 48 + 3 = 51",
         "96", "Calculated for 8 minutes: 12 * 8 = 96"),
         
        ("In a school survey, 3 out of every 5 students prefer pizza over tacos. If 250 students were surveyed, how many students prefer pizza?",
         "150", "150 students",
         "1. Fraction preferring pizza = 3/5. 2. Number of students = (3/5) * 250 = 3 * 50 = 150 students.",
         "100", "Reported students who prefer tacos: (2/5) * 250 = 100",
         "248", "Additive reasoning: 250 - (5-3) = 248"),
         
        ("A store sells 3 pencils for $0.75. How much do 12 pencils cost?",
         "3.00", "$3.00",
         "1. Scale factor: 12 / 3 = 4. 2. Cost = 4 * $0.75 = $3.00.",
         "9.75", "Additive reasoning: 3 + 9 = 12, so 0.75 + 9 = 9.75",
         "2.25", "Calculated for 9 pencils: 3 * 0.75 = 2.25"),
         
        ("The ratio of fiction to non-fiction books in a bin is 5:2. If there are 14 non-fiction books, how many fiction books are there?",
         "35", "35 fiction books",
         "1. Scale factor = 14 / 2 = 7. 2. Fiction books = 5 * 7 = 35.",
         "17", "Additive reasoning: 2 + 12 = 14, so 5 + 12 = 17",
         "49", "Calculated total books: 35 + 14 = 49"),
         
        ("A car travels at a constant speed of 55 miles per hour. How long will it take to travel 220 miles?",
         "4", "4 hours",
         "1. Time = Distance / Speed = 220 / 55 = 4 hours.",
         "165", "Subtracted speed from distance: 220 - 55 = 165",
         "12100", "Multiplied distance by speed: 220 * 55 = 12100"),
         
        ("If 2 centimeters on a drawing represents 8 feet in real life, what is the unit rate in feet per centimeter?",
         "4", "4 feet per centimeter",
         "1. Unit rate = 8 feet / 2 cm = 4 feet per cm.",
         "16", "Multiplied instead of divided: 8 * 2 = 16",
         "0.25", "Inverted ratio: 2 / 8 = 0.25"),
         
        ("A lemonade recipe requires 4 lemons for every 6 cups of water. How many lemons are needed for 15 cups of water?",
         "10", "10 lemons",
         "1. Ratio lemons to water = 4/6 = 2/3. 2. Lemons needed = 15 * (2/3) = 10 lemons.",
         "13", "Additive reasoning: 6 + 9 = 15, so 4 + 9 = 13",
         "22.5", "Cross multiplied backwards: 15 * 6 / 4 = 22.5"),
         
        ("A package of 6 pairs of socks costs $18. How much would 9 pairs of socks cost at the same rate?",
         "27", "$27",
         "1. Unit cost per pair = $18 / 6 = $3. 2. Cost of 9 pairs = 9 * $3 = $27.",
         "21", "Additive reasoning: 6 + 3 = 9, so 18 + 3 = 21",
         "54", "Multiplied 18 * 3 = 54")
    ]
    
    for k, spec in enumerate(ratio_specs, start=51):
        items.append({
            "item_id": f"MATH_G5_{k:03d}",
            "domain": "Ratios & Proportions",
            "domain_code": "RATIO",
            "grade_level": "Grade 5",
            "knowledge_component": "proportional_reasoning_and_rates",
            "problem_text": spec[0],
            "target_answer": spec[1],
            "display_answer": spec[2],
            "solution_steps": spec[3],
            "distractor_d1": spec[4],
            "distractor_d1_reason": spec[5],
            "distractor_d2": spec[6],
            "distractor_d2_reason": spec[7]
        })
        
    # -------------------------------------------------------------
    # Domain 4: Introductory Geometry & Measurement (25 items: 76-100)
    # -------------------------------------------------------------
    geom_specs = [
        ("A rectangular playground is 24 meters long and 15 meters wide. What is the area of the playground in square meters?",
         "360", "360 square meters",
         "1. Area of rectangle = length * width. 2. Area = 24 * 15 = 360 square meters.",
         "78", "Confused perimeter with area: 2*(24 + 15) = 2*39 = 78 meters",
         "39", "Added length and width only: 24 + 15 = 39"),
         
        ("A square garden has a perimeter of 48 feet. What is the length of one side of the garden?",
         "12", "12 feet",
         "1. A square has 4 equal sides. Perimeter = 4 * side. 2. Side length = 48 / 4 = 12 feet.",
         "24", "Divided by 2 instead of 4: 48 / 2 = 24",
         "144", "Squared 12 or confused side with area"),
         
        ("Find the perimeter of a rectangle that has a length of 18 cm and a width of 7 cm.",
         "50", "50 cm",
         "1. Perimeter = 2 * (length + width). 2. Perimeter = 2 * (18 + 7) = 2 * 25 = 50 cm.",
         "126", "Confused area with perimeter: 18 * 7 = 126 square cm",
         "25", "Added length and width once only: 18 + 7 = 25 cm"),
         
        ("A rectangular shoebox has a length of 12 inches, a width of 8 inches, and a height of 5 inches. What is the volume of the box in cubic inches?",
         "480", "480 cubic inches",
         "1. Volume = length * width * height. 2. Volume = 12 * 8 * 5 = 96 * 5 = 480 cubic inches.",
         "25", "Added dimensions together: 12 + 8 + 5 = 25",
         "96", "Calculated base area only: 12 * 8 = 96"),
         
        ("An L-shaped room is formed by joining two non-overlapping rectangles: Rectangle A (6 meters by 4 meters) and Rectangle B (5 meters by 3 meters). What is the total floor area?",
         "39", "39 square meters",
         "1. Area of A = 6 * 4 = 24. 2. Area of B = 5 * 3 = 15. 3. Total area = 24 + 15 = 39 square meters.",
         "18", "Added all side lengths: 6 + 4 + 5 + 3 = 18",
         "72", "Multiplied areas or dimensions together"),
         
        ("A triangle has a base of 14 inches and a height of 8 inches. What is the area of the triangle?",
         "56", "56 square inches",
         "1. Area of triangle = (base * height) / 2. 2. Area = (14 * 8) / 2 = 112 / 2 = 56 square inches.",
         "112", "Forgot to divide by 2: 14 * 8 = 112 (calculated rectangle area)",
         "22", "Added base and height: 14 + 8 = 22"),
         
        ("How many milliliters are in 3.5 liters?",
         "3500", "3,500 milliliters",
         "1. 1 liter = 1,000 milliliters. 2. 3.5 * 1,000 = 3,500 ml.",
         "350", "Multiplied by 100 instead of 1,000: 3.5 * 100 = 350",
         "0.0035", "Divided by 1,000 instead of multiplying"),
         
        ("A movie starts at 2:45 PM and lasts for 1 hour and 50 minutes. What time does the movie end?",
         "4:35 PM", "4:35 PM",
         "1. Add 1 hour: 2:45 PM + 1 hour = 3:45 PM. 2. Add 50 minutes: 45 + 50 = 95 minutes = 1 hour 35 minutes. 3. 3:00 PM + 1h 35m = 4:35 PM.",
         "3:95 PM", "Treated time as base-10: 2.45 + 1.50 = 3.95 PM",
         "4:25 PM", "Calculated 60-minute overflow incorrectly: 4:25 PM"),
         
        ("A rectangular fence encloses a backyard. The length is 30 meters and the width is 20 meters. If fence posts are placed every 5 meters around the entire perimeter, how many posts are needed?",
         "20", "20 posts",
         "1. Perimeter = 2 * (30 + 20) = 100 meters. 2. Number of posts = 100 / 5 = 20 posts.",
         "10", "Calculated posts for half perimeter: 50 / 5 = 10",
         "25", "Counted fence posts on separate sides without corner sharing: 6 + 6 + 4 + 4 + ..."),
         
        ("A wooden cube has edges that are each 6 centimeters long. What is the total surface area of the cube in square centimeters?",
         "216", "216 square centimeters",
         "1. Area of one face = 6 * 6 = 36 sq cm. 2. A cube has 6 identical faces. 3. Total surface area = 6 * 36 = 216 sq cm.",
         "36", "Calculated surface area of only one face",
         "24", "Added side lengths: 6 * 4 = 24"),
         
        ("How many centimeters are in 4.2 meters?",
         "420", "420 centimeters",
         "1. 1 meter = 100 centimeters. 2. 4.2 * 100 = 420 cm.",
         "42", "Multiplied by 10 instead of 100",
         "4200", "Multiplied by 1,000 instead of 100"),
         
        ("A rectangular prism has a base with area 45 square centimeters and a height of 8 centimeters. What is its volume?",
         "360", "360 cubic centimeters",
         "1. Volume = base area * height = 45 * 8 = 360 cubic cm.",
         "53", "Added base area and height: 45 + 8 = 53",
         "180", "Divided by 2 as if a pyramid or triangle: (45 * 8)/2 = 180"),
         
        ("An angle measures 65 degrees. What is the measure of its complementary angle?",
         "25", "25 degrees",
         "1. Complementary angles sum to 90 degrees. 2. Angle = 90 - 65 = 25 degrees.",
         "115", "Confused complementary with supplementary (180 - 65 = 115)",
         "35", "Subtraction regrouping slip: 90 - 65 = 35"),
         
        ("What is the measure of the supplement of an angle that measures 110 degrees?",
         "70", "70 degrees",
         "1. Supplementary angles sum to 180 degrees. 2. Supplement = 180 - 110 = 70 degrees.",
         "20", "Confused with complementary angles (90 - 110 is impossible, or 90 - 70)",
         "80", "Subtraction slip: 180 - 110 = 80"),
         
        ("A rectangular rug is 9 feet long and 6 feet wide. A border tape runs along all 4 edges. How many feet of tape are needed?",
         "30", "30 feet",
         "1. Border tape = perimeter. 2. Perimeter = 2 * (9 + 6) = 2 * 15 = 30 feet.",
         "54", "Calculated area instead of perimeter: 9 * 6 = 54 sq ft",
         "15", "Added length and width once: 9 + 6 = 15 feet"),
         
        ("A pitcher holds 2.4 liters of juice. How many 200-milliliter cups can be completely filled?",
         "12", "12 cups",
         "1. Convert liters to milliliters: 2.4 * 1000 = 2,400 ml. 2. Number of cups = 2400 / 200 = 12 cups.",
         "1.2", "Did not convert units: 2.4 / 200 = 0.012 or 1.2",
         "24", "Divided 2400 by 100 instead of 200"),
         
        ("A triangle has angles measuring 50 degrees and 70 degrees. What is the measure of the third angle?",
         "60", "60 degrees",
         "1. The interior angles of a triangle sum to 180 degrees. 2. Third angle = 180 - (50 + 70) = 180 - 120 = 60 degrees.",
         "120", "Sum of first two angles without subtracting from 180",
         "70", "Guessed isosceles triangle: assumed two angles are equal"),
         
        ("A rectangular picture frame measures 10 inches by 14 inches. What is the area of the glass needed to cover the picture?",
         "140", "140 square inches",
         "1. Area = length * width = 10 * 14 = 140 square inches.",
         "48", "Calculated perimeter: 2*(10 + 14) = 48 inches",
         "24", "Added dimensions: 10 + 14 = 24"),
         
        ("A cardboard box has dimensions 10 cm by 10 cm by 10 cm. What is its volume in cubic centimeters?",
         "1000", "1,000 cubic centimeters",
         "1. Volume of cube = side^3 = 10 * 10 * 10 = 1,000 cubic cm.",
         "100", "Calculated area of one face: 10 * 10 = 100",
         "30", "Added side lengths: 10 + 10 + 10 = 30"),
         
        ("Soccer practice began at 4:15 PM and ended at 5:45 PM. How many minutes long was soccer practice?",
         "90", "90 minutes",
         "1. From 4:15 PM to 5:15 PM is 60 minutes. 2. From 5:15 PM to 5:45 PM is 30 minutes. 3. Total duration = 60 + 30 = 90 minutes.",
         "130", "Treated time as base 100: 545 - 415 = 130",
         "75", "Calculated 1 hour and 15 minutes = 75 minutes"),
         
        ("A rectangular tile is 8 inches long and 4 inches wide. How many tiles are needed to cover a rectangular table that is 32 inches long and 16 inches wide?",
         "16", "16 tiles",
         "1. Area of tile = 8 * 4 = 32 sq in. 2. Area of table = 32 * 16 = 512 sq in. 3. Tiles needed = 512 / 32 = 16 tiles (or (32/8) * (16/4) = 4 * 4 = 16).",
         "8", "Divided dimension by tile length only: 32 / 4 = 8",
         "64", "Multiplied tiles along length by width without dividing: 16 * 4 = 64"),
         
        ("How many grams are in 4.75 kilograms?",
         "4750", "4,750 grams",
         "1. 1 kg = 1,000 g. 2. 4.75 * 1000 = 4,750 grams.",
         "475", "Multiplied by 100 instead of 1000",
         "0.00475", "Divided by 1000 instead of multiplying"),
         
        ("A rectangular garden has a perimeter of 40 meters. If its length is 12 meters, what is its width?",
         "8", "8 meters",
         "1. Perimeter = 2 * (length + width) = 40. 2. length + width = 20. 3. width = 20 - 12 = 8 meters.",
         "28", "Subtracted length from full perimeter: 40 - 12 = 28",
         "16", "Subtracted 24 from 40 = 16 but forgot to divide by 2"),
         
        ("A swimming pool is 25 meters long, 10 meters wide, and 2 meters deep. What is the capacity of the pool in cubic meters?",
         "500", "500 cubic meters",
         "1. Volume = length * width * depth. 2. Volume = 25 * 10 * 2 = 500 cubic meters.",
         "74", "Calculated perimeter: 2 * (25 + 10) + 2 = 72 or 74",
         "250", "Multiplied length by width only: 25 * 10 = 250"),
         
        ("A rectangular track has two straight sides of 80 meters each and two ends that total 40 meters. Jackson runs around the track 3 times. What is the total distance he runs?",
         "600", "600 meters",
         "1. Perimeter of 1 lap = 80 + 80 + 40 = 200 meters. 2. 3 laps = 200 * 3 = 600 meters.",
         "200", "Calculated 1 lap only: 200 meters",
         "360", "Omitted one straight side: (80 + 40) * 3 = 360")
    ]
    
    for m, spec in enumerate(geom_specs, start=76):
        items.append({
            "item_id": f"MATH_G5_{m:03d}",
            "domain": "Introductory Geometry & Measurement",
            "domain_code": "GEOM",
            "grade_level": "Grade 5",
            "knowledge_component": "geometry_and_measurement_foundations",
            "problem_text": spec[0],
            "target_answer": spec[1],
            "display_answer": spec[2],
            "solution_steps": spec[3],
            "distractor_d1": spec[4],
            "distractor_d1_reason": spec[5],
            "distractor_d2": spec[6],
            "distractor_d2_reason": spec[7]
        })
        
    return items

def main():
    items = create_benchmark_items()
    assert len(items) == 100, f"Expected 100 items, got {len(items)}"
    
    # Verify stratification: 25 items per domain
    domains = {}
    for it in items:
        domains[it["domain"]] = domains.get(it["domain"], 0) + 1
    print("Benchmark Stratification:", domains)
    assert all(count == 25 for count in domains.values()), "Each domain must have exactly 25 items!"
    
    out_dir = Path("/home/jason/EdTechPaper1/project_ai_cognitive_debt/data/benchmark_100")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    json_path = out_dir / "benchmark_100.json"
    csv_path = out_dir / "benchmark_100.csv"
    
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2)
    print(f"Saved {json_path}")
    
    keys = list(items[0].keys())
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(items)
    print(f"Saved {csv_path}")

if __name__ == "__main__":
    main()
