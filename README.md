## Creating a Virtual Environment

### On macOS/Linux:

```bash
python3 -m venv .venv
```

The command creates a folder named `.venv` containing the isolated Python environment.

## Activating the Virtual Environment

### On macOS/Linux:

```bash
source .venv/bin/activate
```

## Installing Dependencies

Once activated, install your project requirements:

```bash
pip install -r requirements.txt
```

## vigenere_cipher.py result
Level 1 Vigenere Cipher

Encrypted:
Vyc pkhojt xz rjv agxozfr dm zgrsibtac twplij. Rd ksbvaa hpv rls vctteps rjv ygmwyk ih hpv'j yxf. Hnv cgprkt gh as cyo rhl viyclzgke xurq rldmvki mpulgi mg t bkn mpactzya awy zmeycujgdg cl sepbrkwsa mvoegh. Afg ygvasyk, ah afg cmlxgz, wogt mh tpxmwizsb pq c dmsx cl ruivzkfegtdnp. Twvqg nfd ywtu uvsw ovycbbmj ic icclrxyir khxueu rpt vcxiuea ukkfdnh hvicn ajrpbbbm. Khxz gu r dpnzz. Khdzc yym ubbj sepbrkwsa fsgeicnq ke zttizzfjs rjzlvl oxv twl awcrxoozvd. Uvp vychx hnvrt pq jfnt. Mvkp agl rjv caxqz ko lomo scpnhowua afkeeh fsge ocsw Dvyjmm. Zyegl gu em hnqn khxue cj y bhfgc og hl kdkdkor sodr. Zqfih tfk neas utzrixb, ui bpkja npxmhke. Twhr kj yae. Hnv nxucvvccmv-ivnibpa ughewqv ou ycccghf wy kht yyiv mu Vorzbpu qgvgcz voj olu dctc xg o mcahz. Rjv lxgszvecaf-evlinfe uihsgmv mu Kcsrnipakjk xl hnv rpnc qw Apewhrn cvr uvcxgu nzs ddl hrat bb g xlpzq. Vyc bhfgc lxmc qw kpg tuimh wytk mu mvk juqqcek kpmhki ou afg rpibgz, sui afg dmgtzoky dm ytk adggojth pl vyc exflvci bqg fd pg wsgegmcek ktwwad. Nd hpvzqi wsyzrtz rq gpdos geyiogpx. Ckxb zyicnq vyyi tfk krjl ace zt ifumes. Um cirxlh nrs tafktya lmsgaioggj. Yc xhnzcps qadnpmve zn pu ytkghm wy rn juncibdgohce bhlpvpxla uw sifjg. Em pkhojt xz cxvp bhfhzd. Ioc cirxlh irn tentvqh xjkiyiogpx. Rwhimyt pub nrlvnomv agl rq kft tfzzsi plukpjfstks dm yp rpi. Owiv ack tkirjx oxv td afg rpibgz dailpkrjh ycx rn pyr. Himb mvk goxur qw txxk uw fdyk, vyc irdk ff psj vyc pkhy zs ioc cir dy hnv mjzgezyc. Yfud twl nqzli ht bzel vd hvcabbm, kht havfp'h vfgwt xz rjv rnis. Gcl pyr kj yi hbiv sjydctc pgr ypmqvj. Vymhx knf gd icpvyia hnv sjydctc sh gu rt iocki ntkwr. Khdzc yym gxoj kht zwosma wc yf ai afgzp exfoc. Ii pq vyc hisikaivp, ceb chh rzft, afck ygm fkrlaf kkipdkg. Jzvtyqkkw dy cvznxvl csmjm o cfrz vd cir haccj twhr vyc lhfq zs clu, efkeesd, miihj. Yycc vfokirz bkjyvksk kht hpvzqi bg oe arjmtu uxmv nzmhljh. Nc rtb lfrvptg r kpg tui mprgpx y jlslll iogpx yh ectx ah oc ffch gcz rdbppg zr. Ias ueln lvelqt ycx dazpli r shxzkjs iogpx gh mvgk ocl yfdggxg ok icacpjcar. Orc aga gu hsxms ajealqu.

Decrypted:
The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim. The critic is he who can translate into another manner or a new material his impression of beautiful things. The highest, as the lowest, form of criticism is a mode of autobiography. Those who find ugly meanings in beautiful things are corrupt without being charming. This is a fault. Those who find beautiful meanings in beautiful things are the cultivated. For these there is hope. They are the elect to whom beautiful things mean only Beauty. There is no such thing as a moral or an immoral book. Books are well written, or badly written. That is all. The nineteenth-century dislike of realism is the rage of Caliban seeing his own face in a glass. The nineteenth-century dislike of Romanticism is the rage of Caliban not seeing his own face in a glass. The moral life of man forms part of the subject matter of the artist, but the morality of art consists in the perfect use of an imperfect medium. No artist desires to prove anything. Even things that are true can be proved. No artist has ethical sympathies. An ethical sympathy in an artist is an unpardonable mannerism of style. No artist is ever morbid. The artist can express everything. Thought and language are to the artist instruments of an art. Vice and virtue are to the artist materials for an art. From the point of view of form, the type of all the arts is the art of the musician. From the point of view of feeling, the actor's craft is the type. All art is at once surface and symbol. Those who go beneath the surface do so at their peril. Those who read the symbol do so at their peril. It is the spectator, and not life, that art really mirrors. Diversity of opinion about a work of art shows that the work is new, complex, vital. When critics disagree the artist is in accord with himself. We can forgive a man for making a useful thing as long as he does not admire it. The only excuse for making a useless thing is that one admires it intensely. All art is quite useless.

Level 2 Vigenere Cipher Cryptanalysis

Method 1: Kasiski Examination
Repeated sequences found:
  "VYC" at positions [0, 241, 372, 684, 768, 1116, 1128, 1320, 1404]
  "HNV" at positions [77, 377, 521, 641, 1145, 1253]
  "AFG" at positions [166, 178, 730, 742, 1066, 1306]
  "RJV" at positions [11, 59, 395, 599, 1199]
  "IOG" at positions [825, 885, 993, 1509, 1569]
  "GPX" at positions [827, 995, 1499, 1511, 1571]
  "CIR" at positions [864, 972, 1118, 1140, 1392]
  "HPV" at positions [46, 70, 802, 1450]
  "MVK" at positions [112, 388, 712, 1096]
  "SGE" at positions [329, 425, 786, 821]

Distances between repetitions: [12, 22, 24, 35, 48, 60, 84, 96, 108, 120, 131, 144, 146, 168, 192, 204, 240, 241, 252, 276]

Most common divisors: ['2(39)', '3(37)', '4(37)', '6(37)', '12(37)']
Most likely key length (Kasiski): 2

Method 2: Friedman Test (Index of Coincidence)
Testing key lengths with Index of Coincidence:
(English text IoC ≈ 0.065, Random text IoC ≈ 0.038)

  Key length  1: avg IoC = 0.0409
  Key length  2: avg IoC = 0.0444
  Key length  3: avg IoC = 0.0477
  Key length  4: avg IoC = 0.0469
  Key length  5: avg IoC = 0.0407
  Key length  6: avg IoC = 0.0583
  Key length  7: avg IoC = 0.0406
  Key length  8: avg IoC = 0.0470
  Key length  9: avg IoC = 0.0470
  Key length 10: avg IoC = 0.0444
  Key length 11: avg IoC = 0.0404
  Key length 12: avg IoC = 0.0697
  Key length 13: avg IoC = 0.0401
  Key length 14: avg IoC = 0.0437
  Key length 15: avg IoC = 0.0474
  Key length 16: avg IoC = 0.0462
  Key length 17: avg IoC = 0.0403
  Key length 18: avg IoC = 0.0574
  Key length 19: avg IoC = 0.0406
  Key length 20: avg IoC = 0.0467

Most likely key length: 12 (IoC = 0.0697)

Comparison:
  Kasiski method: 2
  Friedman test:  12

  Using Friedman test result: 12

Recovering key using chi-squared test...

  Position  1: C (chi-squared = 27.30)
  Position  2: R (chi-squared = 31.02)
  Position  3: Y (chi-squared = 32.84)
  Position  4: P (chi-squared = 38.08)
  Position  5: T (chi-squared = 24.53)
  Position  6: O (chi-squared = 22.25)
  Position  7: G (chi-squared = 23.98)
  Position  8: R (chi-squared = 29.54)
  Position  9: A (chi-squared = 21.45)
  Position 10: P (chi-squared = 21.24)
  Position 11: H (chi-squared = 25.52)
  Position 12: Y (chi-squared = 25.18)
Recovered key: CRYPTOGRAPHY
Original key:  CRYPTOGRAPHY

Decrypted with recovered key:
The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim. The critic is he who can translate into another manner or a new material his impression of beautiful things. The highest, as the lowest, form of criticism is a mode of autobiography. Those who find ugly...

## transposition_cipher.py result
LEVEL 1: Simple Columnar Transposition Cipher
Original text: The artist is the creator of beautiful things
Key: SECRET
Encrypted text: ETCRUTXHSEOALSRSEFIIXAIROTHXTIHTEUGTTABFNX
Decrypted text: THEARTISTISTHECREATOROFBEAUTIFULTHINGSXXXX
Integrity verified: Decryption successful!

LEVEL 2: Double Columnar Transposition Cipher
Original text: The artist is the creator of beautiful things
Key 1: SECRET
Key 2: CRYPTO
Final encrypted text: EXLIOHTTAFRITXRESAXUFTHSITTAUOEITGNCSRXHEB

DECRYPTION
Final decrypted text: THEARTISTISTHECREATOROFBEAUTIFULTHINGSXXXX
Integrity verified: Double decryption successful!

## table_cipher.py
LEVEL 1: Table Cipher (Playfair-style)
Original text: The artist is the creator of beautiful things
Key: MATRIX
Generated table:
  M A T R I
  X B C D E
  F G H K L
  N O P Q S
  U V W Y Z
Encrypted text: CPBIIREZRMPILCDTBIAPAQGXBIWMMLZFCPMSLO
Decrypted text: THEARTISTISTHECREATOROFBEAUTIFULTHINGS
Integrity verified: Decryption successful!

LEVEL 2: Combined Cipher (Vigenere + Table)
Original text: The artist is the creator of beautiful things
Vigenere key: CRYPTOGRAPHY
Table key: CRYPTO
Final encrypted text: WRRTFIDFPZVTGXGMUDUKPASVMAQKEYORYZCQQPQP

DECRYPTION
Final decrypted text: THEARTIRTISTGECREATORO