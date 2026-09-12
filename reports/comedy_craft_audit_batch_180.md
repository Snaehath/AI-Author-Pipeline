# Phase 3D.1 Comedy Craft Human Calibration Batch (180 Passages)

## Sampling Strategy & Pool Representation

- **Total Passages Audited:** 180
- **Foundation Candidates (`PURE_MECHANISM`):** 15 (100% of discovered Foundation candidates)
- **Composite Candidates (`COMPOSITE_CRAFT`):** 60
- **PARTIAL Review Queue:** 80 (Testing high-value borderline rescue)
- **NO Negative Controls:** 25 (Testing gate false-negative rate / recall)
- **Distinct Source Works Represented:** 20

### Source Work Representation

| Source Work | Sampled Count |
| :--- | :---: |
| The Little Nugget | 22 |
| My Man Jeeves | 16 |
| A Damsel In Distress | 14 |
| The Man Upstairs | 13 |
| Right Ho | 12 |
| Something Fresh | 12 |
| Three Men In A Boat | 11 |
| The Inimitable Jeeves | 10 |
| Their Mutual Child | 10 |
| Three Men On The Bummel | 10 |
| Love Among The Chickens | 9 |
| Jill The Reckless | 8 |
| The Diary Of A Nobody | 8 |
| The Adventures Of Sally | 7 |
| Piccadilly Jim | 6 |
| Psmith In The City | 4 |
| Idle Thoughts | 3 |
| The Prince And Betty | 3 |
| The Click Of Triangle | 1 |
| Uneasy Money | 1 |

---

## Audit Instructions

For each passage, independently assess:
1. **`craft_presence`**: `YES`, `NO`, or `PARTIAL`
2. **`craft_stratum`**: `PURE_MECHANISM`, `COMPOSITE_CRAFT`, or `REJECT`
3. **`primary_mechanism`**: What is the dominant mechanism? (Independent of detector hypothesis)
4. **`secondary_mechanisms`**: List of co-occurring secondary mechanisms (e.g. ["DEADPAN_REACTION", "VERBAL_WIT"])
5. **`mechanism_horizon`**: `LOCAL` (manifests within scene) vs `LONG_HORIZON` (requires context)
6. **`detector_correct`**: `true` if detector primary matches actual craft, `false` otherwise
7. **`literary_quality`**: 1 to 10 (prose elegance, vocabulary, rhythm, stylistic polish)
8. **`craft_clarity`**: 1 to 10 (unmistakable structural execution of setup, escalation, reversal, payoff)
9. **`training_value`**: 1 to 10 (pedagogical teaching utility for 1.5B specialist SFT/DPO)
10. **`keep_verdict`**: `KEEP` (enters Gold SFT/DPO), `REJECT`, or `REVISE`

---

### Passage 001 [FOUNDATION] — *The Little Nugget* (`the_little_nugget_ch1_01684`)

> "Morgan wired. Not long after this the president of the express company received a letter from Professor Gordon. It was a long and scholarly letter, but the point was that the guinea-pig was the Cava aparoea while the common pig was the genius Sus of the family Suidae. He remarked that they were prolific and multiplied rapidly," " "Sell no pigs, They are not pigs," said the president, decidedly, to Morgan.

- **Detector Prediction:** `YES` | Stratum: `PURE_MECHANISM` | Primary: `ESCALATION` (conf: `0.7`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 8,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": true,
  "notes": "Clear guinea-pig classification premise expands into an absurd bureaucratic problem; the scientific explanation makes the situation more absurd rather than resolving it."
}
```

---

### Passage 002 [FOUNDATION] — *A Damsel In Distress* (`a_damsel_in_distress_ch29_04150`)

> CHAPTER XXVI EVERYBODY HAPPY Jimmy looked at Ann. They were alone. Mr. Pett had gone back to
bed, Mrs. Crocker to her hotel. Mr. Crocker was removing his
make-up in his room. A silence had followed their departure. "This is the end of a perfect day!" said Jimmy. Ann took a step towards the door. "Don't go!" Ann stopped. "Mr. Crocker!" she said. "Jimmy," he corrected. "Mr. Crocker!" repeated Ann firmly. "Or Algernon, if you prefer it." "May I ask--" Ann regarded him steadily. "May I ask." "Nearly always," said Jimmy, "when people begin with that, they
are going to say something unpleasant." "May I ask why you went to all this trouble to make a fool of me?
Why could you not have told me who you were from the start?" "Have you forgotten all the harsh things you said to me from time
to time about Jimmy Crocker? I thought that, if you knew who I
was, you would have nothing more to do with me." "You were quite right." "Surely, though, you won't let a thing that happened five years
ago make so much difference?" "I shall never forgive you!" "And yet, a little while ago, when Willie's bomb was about to go
off, you flung yourself into my arms!" Ann's face flamed. "I lost my balance." "Why try to recover it?" Ann bit her lip. "You did a cruel, heartless thing. What does it matter how long
ago it was? If you were capable of it then--" "Be reasonable. Don't you admit the possibility of reformation?
Take your own case. Five years ago you were a minor poetess. Now
you are an amateur kidnapper--a bright, lovable girl at whose
approach people lock up their children and sit on the key. As for
me, five years ago I was a heartless brute. Now I am a sober
serious business-man, specially called in by your uncle to help
jack up his tottering firm. Why not bury the dead past?
Besides--I don't want to praise myself, I just want to call your
attention to it--think what I have done for you. You admitted
yourself that it was my influence that had revolutionised your
character. But for me, you would now be doing worse than write
poetry. You would be writing _vers libre_. I saved you from that.
And you spurn me!" "I hate you!" said Ann. Jimmy went to the writing-desk and took up a small book. "Put that down!" "I just wanted to read you 'Love's Funeral!' It illustrates my
point. Think of yourself as you are now, and remember that it is
I who am responsible for the improvement. Here we are. 'Love's
Funeral.' 'My heart is dead. . . .' " Ann snatched the book from his hands and flung it away. It soared
up, clearing the gallery rails, and fell with a thud on the
gallery floor. She stood facing him with sparkling eyes. Then she
moved away. "I beg your pardon," she said stiffly. "I lost my temper." "It's your hair," said Jimmy soothingly. "You're bound to be
quick-tempered with hair of that glorious red shade. You must
marry some nice, determined fellow, blue-eyed, dark-haired,
clean-shaven, about five foot eleven, with a future in business.
He will keep you in order." "Mr. Crocker!" "Gently, of course. Kindly-lovingly. The velvet thingummy rather
than the iron what's-its-name. But nevertheless firmly." Ann was at the door. "To a girl with your ardent nature some one with whom you can
quarrel is an absolute necessity of life. You and I are
affinities. Ours will be an ideally happy marriage. You would be
miserable if you had to go through life with a human doormat with
'Welcome' written on him. You want some one made of sterner
stuff. You want, as it were, a sparring-partner, some one with
whom you can quarrel happily with the certain knowledge that he
will not curl up in a ball for you to kick, but will be there
with the return wallop. I may have my faults--" He paused
expectantly. Ann remained silent. "No, no!" he went on. "But I am
such a man. Brisk give-and-take is the foundation of the happy
marriage. Do you remember that beautiful line of Tennyson's--'We
fell out, my wife and I'? It always conjures up for me a vision
of wonderful domestic happiness. I seem to see us in our old age,
you on one side of the radiator, I on the other, warming our old
limbs and thinking up snappy stuff to hand to each
other--sweethearts still! If I were to go out of your life now,
you would be miserable. You would have nobody to quarrel with.
You would be in the position of the female jaguar of the Indian
jungle, who, as you doubtless know, expresses her affection for
her mate by biting him shrewdly in the fleshy part of the leg, if
she should snap sideways one day and find nothing there." Of all the things which Ann had been trying to say during this
discourse, only one succeeded in finding expression. To her
mortification, it was the only weak one in the collection. "Are you asking me to marry you?" "I am." "I won't!" "You think so now, because I am not appearing at my best. You see
me nervous, diffident, tongue-tied. All this will wear off,
however, and you will be surprised and delighted as you begin to
understand my true self. Beneath the surface--I speak
conservatively--I am a corker!" The door banged behind Ann. Jimmy found himself alone. He walked
thoughtfully to Mr. Pett's armchair and sat down. There was a
feeling of desolation upon him. He lit a cigarette and began to
smoke pensively. What a fool he had been to talk like that! What
girl of spirit could possibly stand it? If ever there had been a
time for being soothing and serious and pleading, it had been
these last few minutes. And he talked like that! Ten minutes passed. Jimmy sprang from his chair. He thought he
had heard a footstep. He flung the door open. The passage was
empty. He returned miserably to his chair. Of course she had not
come back. Why should she? A voice spoke. "Jimmy!" He leaped up again, and looked wildly round. Then he looked up.
Ann was leaning over the gallery rail. "Jimmy, I've been thinking it over. There's something I want to
ask you. Do you admit that you behaved abominably five years
ago?" "Yes!" shouted Jimmy. "And that you've been behaving just as badly ever since?" "Yes!" "And that you are really a pretty awful sort of person?" "Yes!" "Then it's all right. You deserve it!" "Deserve it?" "Deserve to marry a girl like me. I was worried about it, but now
I see that it's the only punishment bad enough for you!" She
raised her arm. "Here's the dead past, Jimmy! Go and bury it! Good-night!" A small book fell squashily at Jimmy's feet. He regarded it dully
for a moment. Then, with a wild yell which penetrated even to Mr.
Pett's bedroom and woke that sufferer just as he was dropping off
to sleep for the third time that night he bounded for the gallery
stairs. At the further end of the gallery a musical laugh sounded, and a
door closed. Ann had gone.

- **Detector Prediction:** `YES` | Stratum: `PURE_MECHANISM` | Primary: `ESCALATION` (conf: `0.95`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [
    "VERBAL_WIT",
    "STATUS_REVERSAL"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 10,
  "craft_clarity": 10,
  "training_value": 10,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Extended romantic quarrel repeatedly raises the stakes through Jimmy's increasingly absurd arguments, then reverses the apparent rejection into the marriage 'punishment' payoff."
}
```

---

### Passage 003 [FOUNDATION] — *My Man Jeeves* (`my_man_jeeves_ch6_04598`)

> "And he floated out, leaving us to discuss details. Until we started this business of floating old Chiswick as a money-making proposition I had never realized what a perfectly foul time those Stock Exchange chappies must have when the public isn't biting freely. Nowadays I read that bit they put in the financial reports about," The market opened quietly" with a sympathetic eye, for, by Jove, it certainly opened quietly for us! You'd hardly believe how difficult it was to interest the public and make them take a flutter on the old boy.

- **Detector Prediction:** `YES` | Stratum: `PURE_MECHANISM` | Primary: `DEADPAN_REACTION` (conf: `0.9`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 8,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "The main engine is ironic verbal understatement: the Stock Exchange phrase 'opened quietly' is reapplied to an absurdly unsuccessful scheme in a deadpan voice."
}
```

---

### Passage 004 [FOUNDATION] — *The Little Nugget* (`the_little_nugget_ch1_05736`)

> Speaker: Character | Target Emotion: Hopeful / Reassuring
"said the president," "Then of course guinea-pigs are pigs, Yes," agreed Morgan, "I look at it that way, too.

- **Detector Prediction:** `YES` | Stratum: `PURE_MECHANISM` | Primary: `ESCALATION` (conf: `0.7`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 7,
  "craft_clarity": 8,
  "training_value": 8,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Literal classification of guinea-pigs as pigs drives the joke; the agreement is funny because it accepts the absurd premise."
}
```

---

### Passage 005 [FOUNDATION] — *The Little Nugget* (`the_little_nugget_ch1_05984`)

> "Flannery was crowded into a few feet at the extreme front of the office. The pigs had all the rest of the room and two boys were employed constantly attending to them. The day after Flannery had counted the guinea-pigs there were eight more added to his drove, and by the time the Audit Department gave him authority to collect for eight hundred Flannery had given up all attempts to attend to the receipt or the delivery of goods. He was hastily building galleries around the express office, tier above tier. He had four thousand and sixty-four guinea-pigs to care for! More were arriving daily. Immediately following its authorization the Audit Department sent another letter, but Flannery was too busy to open it. They wrote another and then they telegraphed:," Error in guinea-pig bill.

- **Detector Prediction:** `YES` | Stratum: `PURE_MECHANISM` | Primary: `ESCALATION` (conf: `0.6`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 10,
  "training_value": 10,
  "keep_verdict": "KEEP",
  "detector_correct": true,
  "notes": "Excellent escalation: the guinea-pigs consume the office, multiply into thousands, and the bureaucratic error arrives after the physical absurdity has already become enormous."
}
```

---

### Passage 006 [FOUNDATION] — *The Little Nugget* (`the_little_nugget_ch2_06202`)

> they filled them with guinea-pigs and expressed them to Franklin. Day after day the cages of guineapigs flowed in a steady stream from Westcote to Franklin, and still Flannery and his six helpers ripped and nailed and packed--relentlessly and feverishly. At the end of the week they had shipped two hundred and eighty cases of guinea-pigs, and there were in the express office seven hundred and four more pigs than when they began packing them. "Stop sending pigs. Warehouse full," came a telegram to Flannery. He stopped packing only long enough to wire back, "Can't stop," and kept on sending them. On the next train up from Franklin came one of the company's inspectors. He had instructions to stop the stream of guinea-pigs at all hazards. As his train drew up at Westcote station he saw a cattle car standing on the express company's siding. When he reached the express office he saw the express wagon backed up to the door. Six boys were carrying bushel baskets full of guinea-pigs from the office and dumping them into the wagon. Inside the room Flannery, with' his coat and vest off, was shoveling guinea-pigs into bushel baskets with a coal scoop. He was winding up the guinea-pig episode. He looked up at the inspector with a snort of anger. "Wan wagonload more an, I'll be quit of thim, an' niver will ye catch Flannery wid no more foreign pigs on his hands. No, sur! They near was the death o' me. Nixt toime I'll know that pigs of whaiver nationality is domistic pets--an' go at the lowest rate." He began shoveling again rapidly, speaking quickly between breaths. "Rules may be rules, but you can't fool Mike Flannery twice wid the same thrick--whin ut comes to live stock, dang the rules. So long as Flannery runs this expriss office--pigs is pets--an' cows is pets--an' horses is pets--an' lions an' tigers an' Rocky Mountain goats is pets--an' the rate on thim is twinty-foive cints." He paused long enough to let one of the boys put an empty basket in the place of the one he had just filled. There were only a few guinea-pigs left. As he noted their limited number his natural habit of looking on the bright side returned. "Well, annyhow," he said cheerfully, "'tis not so bad as ut might be. What if thim dago pigs had been elephants!"

- **Detector Prediction:** `YES` | Stratum: `PURE_MECHANISM` | Primary: `ESCALATION` (conf: `0.98`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 10,
  "craft_clarity": 10,
  "training_value": 10,
  "keep_verdict": "KEEP",
  "detector_correct": true,
  "notes": "Flagship escalation example: continual shipments, warehouse overflow, frantic packing, inspector arrival, then Flannery's absurd extension of the pet-rate rule to larger animals."
}
```

---

### Passage 007 [FOUNDATION] — *My Man Jeeves* (`my_man_jeeves_ch16_06214`)

> "I gave a sharp wail of agony. It hadn't struck me till then that Rocky was depending on my wardrobe to see him through," You'll ruin them!" "I hope so," said Rocky, in the most unpleasant way.

- **Detector Prediction:** `YES` | Stratum: `PURE_MECHANISM` | Primary: `PHYSICAL_COMPLICATION` (conf: `0.7`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 8,
  "craft_clarity": 8,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "The comic turn is verbal: the narrator's distress over his wardrobe is answered by Rocky's cheerfully hostile 'I hope so.' The deadpan hostility supplies the finish."
}
```

---

### Passage 008 [FOUNDATION] — *The Little Nugget* (`the_little_nugget_ch1_06292`)

> "Mr. Morgan, the head of the Tariff Department, consulted the president of the Interurban Express Company regarding guinea-pigs, as to whether they were pigs or not pigs. The president was inclined to treat the matter lightly," "If I know signs of refusal, the con-sign-y refuses to pay for wan dang kebbage leaf an' be hanged to me! What is the rate on pigs and on pets?" he asked.

- **Detector Prediction:** `YES` | Stratum: `PURE_MECHANISM` | Primary: `ESCALATION` (conf: `0.95`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 7,
  "craft_clarity": 8,
  "training_value": 8,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "The pig/pet tariff distinction is treated with absurd literal seriousness; the dialogue turns a bureaucratic question into a comic semantic problem."
}
```

---

### Passage 009 [FOUNDATION] — *The Little Nugget* (`the_little_nugget_ch1_06349`)

> Speaker: Do | Target Emotion: Calm / Conversational
"said Flannery," "Do you mean to say that two little guinea-pigs--" "Eight! Papa an' mamma an' the six childer.

- **Detector Prediction:** `YES` | Stratum: `PURE_MECHANISM` | Primary: `ESCALATION` (conf: `0.7`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "REJECT",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": true,
  "literary_quality": 6,
  "craft_clarity": 5,
  "training_value": 5,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "There is a genuine comic beat in the jump from two guinea-pigs to eight, but the excerpt is too fragmentary to establish a reliable craft structure for training."
}
```

---

### Passage 010 [FOUNDATION] — *My Man Jeeves* (`my_man_jeeves_ch16_07705`)

> "And I staggered out. You know, I rather think I agree with those poet-and-philosopher Johnnies who insist that a fellow ought to be devilish pleased if he has a bit of trouble. All that stuff about being refined by suffering, you know. Suffering does give a chap a sort of broader and more sympathetic outlook. It helps you to understand other people's misfortunes if you've been through the same thing yourself. As I stood in my lonely bedroom at the hotel, trying to tie my white tie myself, it struck me for the first time that there must be whole squads of chappies in the world who had to get along without a man to look after them. I'd always thought of [COMPANION] as a kind of natural phenomenon; but, by Jove! of course, when you come to think of it, there must be quite a lot of fellows who have to press their own clothes themselves and haven't got anybody to bring them tea in the morning, and so on. It was rather a solemn thought, don't you know. I mean to say, ever since then I've been able to appreciate the frightful privations the poor have to stick. I got dressed somehow. [COMPANION] hadn't forgotten a thing in his packing. Everything was there, down to the final stud. I'm not sure this didn't make me feel worse. It kind of deepened the pathos. It was like what somebody or other wrote about the touch of a vanished hand. I had a bit of dinner somewhere and went to a show of some kind; but nothing seemed to make any difference. I simply hadn't the heart to go on to supper anywhere. I just sucked down a whisky-and-soda in the hotel smoking-room and went straight up to bed. I don't know when I've felt so rotten. Somehow I found myself moving about the room softly, as if there had been a death in the family. If I had anybody to talk to I should have talked in a whisper; in fact, when the telephone-bell rang I answered in such a sad, hushed voice that the fellow at the other end of the wire said," Halloa!" five times, thinking he hadn't got me.

- **Detector Prediction:** `YES` | Stratum: `PURE_MECHANISM` | Primary: `ESCALATION` (conf: `0.6`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "DEADPAN_REACTION",
  "secondary_mechanisms": [
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Comic engine is the narrator treating the loss of his attendant as a near-death bereavement, with increasingly solemn overstatement and a deadpan telephone payoff."
}
```

---

### Passage 011 [FOUNDATION] — *The Little Nugget* (`the_little_nugget_ch2_07923`)

> Speaker: Character | Target Emotion: Fearful
"'tis not so bad as ut might be. What if thim dago pigs had been elephants!," "Well, annyhow," he said cheerfully,.

- **Detector Prediction:** `YES` | Stratum: `PURE_MECHANISM` | Primary: `ESCALATION` (conf: `0.7`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "REJECT",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": true,
  "literary_quality": 7,
  "craft_clarity": 5,
  "training_value": 5,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "The elephant hypothetical is funny hyperbolic escalation, but the excerpt is only a punchline fragment and is not sufficient as a standalone craft example."
}
```

---

### Passage 012 [FOUNDATION] — *The Man Upstairs* (`the_man_upstairs_ch11_09109`)

> "when speaking of a man. He is handsome enough, heaven knows; I should not even care to trust you with him - faithful of all possible wives that you are - when he looks his best, as he always does. Nor do I think the fascination of his manner has much to do with it. You recollect that the charm of art inheres in that which is undefinable, and to you and me, my dear Irene, I fancy there is rather less of that in the branch of art under consideration than to girls in their first season. I fancy I know how my fine gentleman produces many of his effects, and could, perhaps, give him a pointer on heightening them. Nevertheless, his manner is something truly delightful. I suppose what interests me chiefly is the man's brains. His conversation is the best I have ever heard, and altogether unlike anyone's else. He seems to know everything, as, indeed, he ought, for he has been everywhere, read everything, seen all there is to see - sometimes I think rather more than is good for him - and had acquaintance with the QUEEREST people. And then his voice - Irene, when I hear it I actually feel as if I ought to have PAID AT THE DOOR, though, of course, it is my own door. July 3d. I fear my remarks about Dr. Barritz must have been, being thoughtless, very silly, or you would not have written of him with such levity, not to say disrespect. Believe me, dearest, he has more dignity and seriousness (of the kind, I mean, which is not inconsistent with a manner sometimes playful and always charming) than any of the men that you and I ever met. And young Raynor - you knew Raynor at Monterey - tells me that the men all like him, and that he is treated with something like deference everywhere. There is a mystery, too - something about his connection with the Blavatsky people in Northern India. Raynor either would not or could not tell me the particulars. I infer that Dr. Barritz is thought - don't you dare to laugh at me - a magician! Could anything be finer than that? An ordinary mystery is not, of course, as good as a scandal, but when it relates to dark and dreadful practices - to the exercise of unearthly powers - could anything be more piquant? It explains, too, the singular influence the man has upon me. It is the undefinable in his art - black art. Seriously, dear, I quite tremble when he looks me full in the eyes with those unfathomable orbs of his, which I have already vainly attempted to describe to you. How dreadful if we have the power to make one fall in love! Do you know if the Blavatsky crowd have that power - outside of Sepoy? July 1 The strangest thing! Last evening while Auntie was attending one of the hotel hops (I hate them) Dr. Barritz called. It was scandalously late - I actually believe he had talked with Auntie in the ballroom, and learned from her that I was alone. I had been all the evening contriving how to worm out of him the truth about his connection with the Thugs in Sepoy, and all of that black business, but the moment he fixed his eyes on me (for I admitted him, I'm ashamed to say) I was helpless, I trembled, I blushed, I - O Irene, Irene, I love the man beyond expression, and you know how it is yourself! Fancy! I, an ugly duckling from Redhorse - daughter (they say) of old Calamity Jim - certainly his heiress, with no living relation but an absurd old aunt, who spoils me a thousand and fifty ways - absolutely destitute of everything but a million dollars and a hope in Paris - I daring to love a god like him! My dear, if I had you here, I could tear your hair out with mortification. I am convinced that he is aware of my feeling, for he stayed but a few moments, said nothing but what another man might have said half as well, and pretending that he had an engagement went away. I learned to-day (a little bird told me - the bell bird) that he went straight to bed. How does that strike you as evidence of exemplary habits? July 17th. That little wretch, Raynor, called yesterday, and his babble set me almost wild. He never runs down - that is to say, when he exterminates a score of reputations, more or less, he does not pause between one reputation and the next. (By the way, he inquired about you, and his manifestations of interest in you had, I confess, a good deal of vraisemblance.) Mr. Raynor observes no game laws; like Death (which he would inflict if slander were fatal) he has all seasons for his own. But I like him, for we knew one another at Redhorse when we were young and true-hearted and barefooted. He was known in those far fair days as," It is not, I am sure, his - do you know any noun corresponding to the adjective "handsome"? One does not like to say "beauty Giggles," and I - O Irene, can you ever forgive me? - I was called "Gunny.

- **Detector Prediction:** `YES` | Stratum: `PURE_MECHANISM` | Primary: `SOCIAL_EMBARRASSMENT` (conf: `0.98`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "PARTIAL",
  "craft_stratum": "REJECT",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [
    "SOCIAL_EMBARRASSMENT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 8,
  "craft_clarity": 4,
  "training_value": 2,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Contains witty phrasing and self-mocking romantic exaggeration, but most of the passage is earnest romantic/dramatic material rather than a clean British comic engine."
}
```

---

### Passage 013 [FOUNDATION] — *The Little Nugget* (`the_little_nugget_ch1_09606`)

> "Morgan made the proper notation on the papers that had accumulated in File A6754, and turned them over to the Audit Department. The Audit Department took some time to look the matter up, and after the usual delay wrote Flannery that as he had on hand one hundred and sixty guinea-pigs, the property of consignee, he should deliver them and collect charges at the rate of twenty-five cents each. Flannery spent a day herding his charges through a narrow opening in their cage so that he might count them," Audit Dept.

- **Detector Prediction:** `YES` | Stratum: `PURE_MECHANISM` | Primary: `ESCALATION` (conf: `0.85`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": true,
  "notes": "The absurd administrative task grows into physically herding 160 guinea-pigs; the mismatch between bureaucracy and reality is the comic engine."
}
```

---

### Passage 014 [FOUNDATION] — *The Little Nugget* (`the_little_nugget_ch1_10110`)

> "Mr. Morehouse had moved! Flannery ran all the way back to the express office. Sixty-nine guinea-pigs had been born during his absence. He ran out again and made feverish inquiries in the village. Mr. Morehouse had not only moved, but he had left Westcote. Flannery returned to the express office and found that two hundred and six guinea-pigs had entered the world since he left it. He wrote a telegram to the Audit Department," Can't collect fifty cents for two dago pigs consignee has left town address unknown what shall I do? Flannery.

- **Detector Prediction:** `YES` | Stratum: `PURE_MECHANISM` | Primary: `ESCALATION` (conf: `0.6`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 10,
  "training_value": 10,
  "keep_verdict": "KEEP",
  "detector_correct": true,
  "notes": "Strong escalation: Flannery returns to find dozens and then hundreds more pigs, while the original consignee has disappeared, forcing an increasingly impossible administrative problem."
}
```

---

### Passage 015 [FOUNDATION] — *The Little Nugget* (`the_little_nugget_ch1_10395`)

> "The president put the papers on his desk and wrote a letter to Professor Gordon. Unfortunately the Professor was in South America collecting zoological specimens, and the letter was forwarded to him by his wife. As the Professor was in the highest Andes, where no white man had ever penetrated, the letter was many months in reaching him. The president forgot the guinea-pigs, Morgan forgot them, Mr. Morehouse forgot them, but Flannery did not. One-half of his time he gave to the duties of his agency; the other half was devoted to the guinea-pigs. Long before Professor Gordon received the president's letter Morgan received one from Flannery," About them dago pigs," it said, "what shall I do they are great in family life, no race suicide for them, there are thirty-two now shall I sell them do you take this express office for a menagerie, answer quick.

- **Detector Prediction:** `YES` | Stratum: `PURE_MECHANISM` | Primary: `ESCALATION` (conf: `0.98`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 10,
  "keep_verdict": "KEEP",
  "detector_correct": true,
  "notes": "The forgotten guinea-pigs quietly multiply while officials forget the problem; Flannery's increasingly desperate letter supplies a strong comic escalation and verbal payoff."
}
```

---

### Passage 016 [COMPOSITE] — *A Damsel In Distress* (`a_damsel_in_distress_ch13_09002`)

> CHAPTER X INSTRUCTION IN DEPORTMENT While the feast of reason and flow of soul had been in progress
in the drawing-room, in the gymnasium on the top floor Jerry
Mitchell, awaiting the coming of Mr. Pett, had been passing the
time in improving with strenuous exercise his already impressive
physique. If Mrs. Pett's guests had been less noisily
concentrated on their conversation, they might have heard the
muffled _tap-tap-tap_ that proclaimed that Jerry Mitchell was
punching the bag upstairs. It was not until he had punched it for perhaps five minutes that,
desisting from his labours, he perceived that he had the pleasure
of the company of little Ogden Ford. The stout boy was standing
in the doorway, observing him with an attentive eye. "What are you doing?" enquired Ogden. Jerry passed a gloved fist over his damp brow. "Punchin' the bag." He began to remove his gloves, eyeing Ogden the while with a
disapproval which he made no attempt to conceal. An extremist on
the subject of keeping in condition, the spectacle of the bulbous
stripling was a constant offence to him. Ogden, in pursuance of
his invariable custom on the days when Mrs. Pett entertained, had
been lurking on the stairs outside the drawing-room for the past
hour, levying toll on the food-stuffs that passed his way. He
wore a congested look, and there was jam about his mouth. "Why?" he said, retrieving a morsel of jam from his right cheek
with the tip of his tongue. "To keep in condition." "Why do you want to keep in condition?" Jerry flung the gloves into their locker. "Fade!" he said wearily. "Fade!" "Huh?" "Beat it!" "Huh?" Much pastry seemed to have clouded the boy's mind. "Run away." "Don't want to run away." The annoyed pugilist sat down and scrutinised his visitor
critically. "You never do anything you don't want to, I guess?" "No," said Ogden simply. "You've got a funny nose," he added
dispassionately. "What did you do to it to make it like that?" Mr. Mitchell shifted restlessly on his chair. He was not a vain
man, but he was a little sensitive about that particular item in
his make-up. "Lizzie says it's the funniest nose she ever saw. She says it's
something out of a comic supplement." A dull flush, such as five minutes with the bag had been unable
to produce, appeared on Jerry Mitchell's peculiar countenance. It
was not that he looked on Lizzie Murphy, herself no Lillian
Russell, as an accepted authority on the subject of facial
beauty; but he was aware that in this instance she spoke not
without reason, and he was vexed, moreover, as many another had
been before him, by the note of indulgent patronage in Ogden's
voice. His fingers twitched a little eagerly, and he looked
sullenly at his tactless junior. "Get out!" "Huh?" "Get outa here!" "Don't want to get out of here," said Ogden with finality. He put
his hand in his trouser-pocket and pulled out a sticky mass which
looked as if it might once have been a cream-puff or a meringue.
He swallowed it contentedly. "I'd forgotten I had that," he
explained. "Mary gave it to me on the stairs. Mary thinks you've
a funny nose, too," he proceeded, as one relating agreeable
gossip. "Can it! Can it!" exclaimed the exasperated pugilist. "I'm only telling you what I heard her say." Mr. Mitchell rose convulsively and took a step towards his
persecutor, breathing noisily through the criticised organ. He
was a chivalrous man, a warm admirer of the sex, but he was
conscious of a wish that it was in his power to give Mary what he
would have described as "hers." She was one of the parlour-maids,
a homely woman with a hard eye, and it was part of his grievance
against her that his Maggie, alias Celestine, Mrs. Pett's maid,
had formed an enthusiastic friendship with her. He had no
evidence to go on, but he suspected Mary of using her influence
with Celestine to urge the suit of his leading rival for the
latter's hand, Biggs the chauffeur. He disliked Mary intensely,
even on general grounds. Ogden's revelation added fuel to his
aversion. For a moment he toyed with the fascinating thought of
relieving his feelings by spanking the boy, but restrained
himself reluctantly at the thought of the inevitable ruin which
would ensue. He had been an inmate of the house long enough to
know, with a completeness which would have embarrassed that
gentleman, what a cipher Mr. Pett was in the home and how little
his championship would avail in the event of a clash with Mrs.
Pett. And to give Ogden that physical treatment which should long
since have formed the main plank in the platform of his education
would be to invite her wrath as nothing else could. He checked
himself, and reached out for the skipping-rope, hoping to ease
his mind by further exercise. Ogden, chewing the remains of the cream-puff, eyed him with
languid curiosity. "What are you doing that for?" Mr. Mitchell skipped grimly on. "What are you doing that for? I thought only girls skipped." Mr. Mitchell paid no heed. Ogden, after a moment's silent
contemplation, returned to his original train of thought. "I saw an advertisement in a magazine the other day of a sort of
machine for altering the shape of noses. You strap it on when you
go to bed. You ought to get pop to blow you to one." Jerry Mitchell breathed in a laboured way. "You want to look nice about the place, don't you? Well, then!
there's no sense in going around looking like that if you don't
have to, is there? I heard Mary talking about your nose to Biggs
and Celestine. She said she had to laugh every time she saw it." The skipping-rope faltered in its sweep, caught in the skipper's
legs, and sent him staggering across the room. Ogden threw back
his head and laughed merrily. He liked free entertainments, and
this struck him as a particularly enjoyable one. There are moments in the life of every man when the impulse
attacks him to sacrifice his future to the alluring gratification
of the present. The strong man resists such impulses. Jerry
Mitchell was not a weak man, but he had been sorely tried. The
annoyance of Ogden's presence and conversation had sapped his
self-restraint, as dripping water will wear away a rock. A short
while before, he had fought down the urgent temptation to
massacre this exasperating child, but now, despised love adding
its sting to that of injured vanity, he forgot the consequences.
Bounding across the room, he seized Ogden in a powerful grip, and
the next instant the latter's education, in the true sense of the
word, so long postponed, had begun; and with it that avalanche of
sound which, rolling down into the drawing-room, hurled Mrs. Pett
so violently and with such abruptness from the society of her
guests. Disposing of the last flight of stairs with the agility of the
chamois which leaps from crag to crag of the snow-topped Alps,
Mrs. Pett finished with a fine burst of speed along the passage
on the top floor, and rushed into the gymnasium just as Jerry's
avenging hand was descending for the eleventh time.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `ESCALATION` (conf: `0.25`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [
    "SOCIAL_EMBARRASSMENT",
    "PHYSICAL_COMPLICATION",
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 10,
  "craft_clarity": 10,
  "training_value": 10,
  "keep_verdict": "KEEP",
  "detector_correct": true,
  "notes": "Excellent farce: Ogden repeatedly attacks Jerry's vanity, the irritation escalates, restraint breaks, and the physical consequences explode into the arrival of Mrs. Pett."
}
```

---

### Passage 017 [COMPOSITE] — *Jill The Reckless* (`jill_the_reckless_ch2_06634`)

> "Anne!  Anne!," said Croisette, rising on his elbow and speaking to me
some three hours later, "what do you think the Vidame meant this
morning when he said that about the ten days?".

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 6,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "A request for clarification about an earlier statement; no self-contained comic mechanism is established."
}
```

---

### Passage 018 [COMPOSITE] — *Love Among The Chickens* (`love_among_the_chickens_chNone_09348`)

> "  But Yanson succeeded in repeating once more, convincingly and weightily:  "Why must I be hanged?"  He looked so absurd, with his small, angry face, with his outstretched finger, that even the soldier of the convoy, breaking the rule, said to him in an undertone as he led him away from the courtroom:  "You are a fool, young man!"  "Why must I be hanged?" repeated Yanson stubbornly

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "REJECT",
  "primary_mechanism": "DEADPAN_REACTION",
  "secondary_mechanisms": [
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": true,
  "literary_quality": 7,
  "craft_clarity": 4,
  "training_value": 4,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "There is dark absurdity in the repeated question and the soldier's blunt response, but the passage lacks enough structure to be a strong transferable British-comedy craft example."
}
```

---

### Passage 019 [COMPOSITE] — *My Man Jeeves* (`my_man_jeeves_ch5_07410`)

> "Thank you, sir," "[COMPANION]," I said, "you are certainly a life-saver!" "Nothing would have convinced my Aunt Agatha that I hadn't lured that blighter into riotous living.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "PARTIAL",
  "craft_stratum": "REJECT",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 7,
  "craft_clarity": 3,
  "training_value": 3,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Suggests a comic misunderstanding involving Aunt Agatha and 'riotous living', but the excerpt is too short to establish the mechanism."
}
```

---

### Passage 020 [COMPOSITE] — *Right Ho* (`right_ho_ch12_00604`)

> He gave a kind of grunt of surprise at the first paragraph. "Well, I'm hanged!" he said, as he finished. "Reggie, this is a queer thing." "What's that?" He handed me the letter, and directly I started in on it I saw why he had grunted. This is how it ran: "My dear [COMPANION_B] - I shall be seeing you to-morrow, I hope; but I think it is better, before we meet, to prepare you for a curious situation that has arisen in connection with the legacy which your father inherited from your Aunt Emily, and which you are expecting me, as trustee, to hand over to you, now that you have reached your twenty-fifth birthday. You have doubtless heard your father speak of your twin-brother Alfred, who was lost or kidnapped - which, was never ascertained - when you were both babies. When no news was received of him for so many years, it was supposed that he was dead. Yesterday, however, I received a letter purporting that he had been living all this time in Buenos Ayres as the adopted son of a wealthy South American, and has only recently discovered his identity. He states that he is on his way to meet me, and will arrive any day now. Of course, like other claimants, he may prove to be an impostor, but meanwhile his intervention will, I fear, cause a certain delay before I can hand over your money to you. It will be necessary to go into a thorough examination of credentials, etc., and this will take some time. But I will go fully into the matter with you when we meet. - Your affectionate uncle, "AUGUSTUS ARBUTT." I read it through twice, and the second time I had one of those ideas I do sometimes get, though admittedly a chump of the premier class. I have seldom had such a thoroughly corking brain-wave. "Why, old top," I said, "this lets you out." "Lets me out of half the darned money, if that's what you mean. If this chap's not an imposter - and there's no earthly reason to suppose he is, though I've never heard my father say a word about him - we shall have to split the money. Aunt Emily's will left the money to my father, or, failing him, his 'offspring.' I thought that meant me, but apparently there are a crowd of us. I call it rotten work, springing unexpected offspring on a fellow at the eleventh hour like this." "Why, you chump," I said, "it's going to save you. This lets you out of your spectacular dash across the frontier. All you've got to do is to stay here and be your brother Alfred. It came to me in a flash." He looked at me in a kind of dazed way. "You ought to be in some sort of a home, Reggie." "Ass!" I cried. "Don't you understand? Have you ever heard of twin-brothers who weren't exactly alike? Who's to say you aren't Alfred if you swear you are? Your uncle will be there to back you up that you have a brother Alfred." "And Alfred will be there to call me a liar." "He won't. It's not as if you had to keep it up for the rest of your life. It's only for an hour or two, till we can get this detective off the yacht. We sail for England to-morrow morning." At last the thing seemed to sink into him. His face brightened. "Why, I really do believe it would work," he said. "Of course it would work. If they want proof, show them your mole. I'll swear [COMPANION_B] hadn't one." "And as Alfred I should get a chance of talking to Stella and making things all right for [COMPANION_B]. Reggie, old top, you're a genius." "No, no." "You _are_." "Well, it's only sometimes. I can't keep it up." And just then there was a gentle cough behind us. We spun round. "What the devil are you doing here, Voules," I said. "I beg your pardon, sir. I have heard all." I looked at [COMPANION_B]. [COMPANION_B] looked at me. "Voules is all right," I said. "Decent Voules! Voules wouldn't give us away, would you, Voules?" "Yes, sir." "You would?" "Yes, sir." "But, Voules, old man," I said, "be sensible. What would you gain by it?" "Financially, sir, nothing." "Whereas, by keeping quiet" - I tapped him on the chest - "by holding your tongue, Voules, by saying nothing about it to anybody, Voules, old fellow, you might gain a considerable sum." "Am I to understand, sir, that, because you are rich and I am poor, you think that you can buy my self-respect?" "Oh, come!" I said. "How much?" said Voules. So we switched to terms. You wouldn't believe the way the man haggled. You'd have thought a decent, faithful servant would have been delighted to oblige one in a little matter like that for a fiver. But not Voules. By no means. It was a hundred down, and the promise of another hundred when we had got safely away, before he was satisfied. But we fixed it up at last, and poor old [COMPANION_B] got down to his state-room and changed his clothes. He'd hardly gone when the breakfast-party came on deck. "Did you meet him?" I asked. "Meet whom?" said old Marshall. "[COMPANION_B]'s twin-brother Alfred." "I didn't know [COMPANION_B] had a brother." "Nor did he till yesterday. It's a long story. He was kidnapped in infancy, and everyone thought he was dead. [COMPANION_B] had a letter from his uncle about him yesterday. I shouldn't wonder if that's where [COMPANION_B] has gone, to see his uncle and find out about it. In the meantime, Alfred has arrived. He's down in [COMPANION_B]'s state-room now, having a brush-up. It'll amaze you, the likeness between them. You'll think it _is_ [COMPANION_B] at first. Look! Here he comes." And up came [COMPANION_B], brushed and clean, in an ordinary yachting suit. They were rattled. There was no doubt about that. They stood looking at him, as if they thought there was a catch somewhere, but weren't quite certain where it was. I introduced him, and still they looked doubtful. "Mr. Pepper tells me my brother is not on board," said [COMPANION_B]. "It's an amazing likeness," said old Marshall. "Is my brother like me?" asked [COMPANION_B] amiably. "No one could tell you apart," I said. "I suppose twins always are alike," said [COMPANION_B]. "But if it ever came to a question of identification, there would be one way of distinguishing us. Do you know [COMPANION_B] well, Mr. Pepper?" "He's a dear old pal of mine." "You've been swimming with him perhaps?" "Every day last August." "Well, then, you would have noticed it if he had had a mole like this on the back of his neck, wouldn't you?" He turned his back and stooped and showed the mole. His collar hid it at ordinary times. I had seen it often when we were bathing together. "Has [COMPANION_B] a mole like that?" he asked. "No," I said. "Oh, no." "You would have noticed it if he had?" "Yes," I said. "Oh, yes." "I'm glad of that," said [COMPANION_B]. "It would be a nuisance not to be able to prove one's own identity." That seemed to satisfy them all. They couldn't get away from it. It seemed to me that from now on the thing was a walk-over. And I think [COMPANION_B] felt the same, for, when old Marshall asked him if he had had breakfast, he said he had not, went below, and pitched in as if he hadn't a care in the world. Everything went right till lunch-time. [COMPANION_B] sat in the shade on the foredeck talking to Stella most of the time. When the gong went and the rest had started to go below, he drew me back. He was beaming. "It's all right," he said. "What did I tell you?" "What did you tell me?" "Why, about Stella. Didn't I say that Alfred would fix things for [COMPANION_B]? I told her she looked worried, and got her to tell me what the trouble was. And then - - " "You must have shown a flash of speed if you got her to confide in you after knowing you for about two hours." "Perhaps I did," said [COMPANION_B] modestly, "I had no notion, till I became him, what a persuasive sort of chap my brother Alfred was. Anyway, she told me all about it, and I started in to show her that [COMPANION_B] was a pretty good sort of fellow on the whole, who oughtn't to be turned down for what was evidently merely temporary insanity. She saw my point." "And it's all right?" "Absolutely, if only we can produce [COMPANION_B]. How much longer does that infernal sleuth intend to stay here? He seems to have taken root." "I fancy he thinks that you're bound to come back sooner or later, and is waiting for you." "He's an absolute nuisance," said [COMPANION_B]. We were moving towards the companion way, to go below for lunch, when a boat hailed us. We went to the side and looked over. "It's my uncle," said [COMPANION_B]. A stout man came up the gangway. "Halloa, [COMPANION_B]!" he said. "Get my letter?" "I think you are mistaking me for my brother," said [COMPANION_B]. "My name is Alfred Lattaker." "What's that?" "I am [COMPANION_B]'s brother Alfred. Are you my Uncle Augustus?" The stout man stared at him. "You're very like [COMPANION_B]," he said. "So everyone tells me." "And you're really Alfred?" "I am." "I'd like to talk business with you for a moment." He cocked his eye at me. I sidled off and went below. At the foot of the companion-steps I met Voules. "I beg your pardon, sir," said Voules. "If it would be convenient I should be glad to have the afternoon off." I'm bound to say I rather liked his manner. Absolutely normal. Not a trace of the fellow-conspirator about it. I gave him the afternoon off. I had lunch - [COMPANION_B] didn't show up - and as I was going out I was waylaid by the girl Pilbeam. She had been crying. "I beg your pardon, sir, but did Mr. Voules ask you for the afternoon?" I didn't see what business if was of hers, but she seemed all worked up about it, so I told her. "Yes, I have given him the afternoon off." She broke down - absolutely collapsed. Devilish unpleasant it was. I'm hopeless in a situation like this. After I'd said, "There, there!" which didn't seem to help much, I hadn't any remarks to make. "He s-said he was going to the tables to gamble away all his savings and then shoot himself, because he had nothing left to live for." I suddenly remembered the scrap in the small hours outside my state-room door. I hate mysteries. I meant to get to the bottom of this. I couldn't have a really first-class valet like Voules going about the place shooting himself up. Evidently the girl Pilbeam was at the bottom of the thing. I questioned her. She sobbed. I questioned her more. I was firm. And eventually she yielded up the facts. Voules had seen [COMPANION_B] kiss her the night before; that was the trouble. Things began to piece themselves together. I went up to interview [COMPANION_B]. There was going to be another job for persuasive Alfred. Voules's mind had got to be eased as Stella's had been. I couldn't afford to lose a fellow with his genius for preserving a trouser-crease. I found [COMPANION_B] on the foredeck. What is it Shakespeare or somebody says about some fellow's face being sicklied o'er with the pale cast of care? [COMPANION_B]'s was like that. He looked green. "Finished with your uncle?" I said. He grinned a ghostly grin. "There isn't any uncle," he said. "There isn't any Alfred. And there isn't any money." "Explain yourself, old top," I said. "It won't take long. The old crook has spent every penny of the trust money. He's been at it for years, ever since I was a kid. When the time came to cough up, and I was due to see that he did it, he went to the tables in the hope of a run of luck, and lost the last remnant of the stuff. He had to find a way of holding me for a while and postponing the squaring of accounts while he got away, and he invented this twin-brother business. He knew I should find out sooner or later, but meanwhile he would be able to get off to South America, which he has done. He's on his way now." "You let him go?" "What could I do? I can't afford to make a fuss with that man Sturgis around. I can't prove there's no Alfred when my only chance of avoiding prison is to be Alfred." "Well, you've made things right for yourself with Stella Vanderley, anyway," I said, to cheer him up. "What's the good of that now? I've hardly any money and no prospects. How can I marry her?" I pondered. "It looks to me, old top," I said at last, "as if things were in a bit of a mess." "You've guessed it," said poor old [COMPANION_B]. I spent the afternoon musing on Life. If you come to think of it, what a queer thing Life is! So unlike anything else, don't you know, if you see what I mean. At any moment you may be strolling peacefully along, and all the time Life's waiting around the corner to fetch you one. You can't tell when you may be going to get it. It's all dashed puzzling. Here was poor old [COMPANION_B], as well-meaning a fellow as ever stepped, getting swatted all over the ring by the hand of Fate. Why? That's what I asked myself. Just Life, don't you know. That's all there was about it. It was close on six o'clock when our third visitor of the day arrived. We were sitting on the afterdeck in the cool of the evening - old Marshall, Denman Sturgis, Mrs. Vanderley, Stella, [COMPANION_B], and I - when he came up. We had been talking of [COMPANION_B], and old Marshall was suggesting the advisability of sending out search-parties. He was worried. So was Stella Vanderley. So, for that matter, were [COMPANION_B] and I, only not for the same reason. We were just arguing the thing out when the visitor appeared. He was a well-built, stiff sort of fellow. He spoke with a German accent. "Mr. Marshall?" he said. "I am Count Fritz von Cöslin, equerry to His Serene Highness" - he clicked his heels together and saluted - "the Prince of Saxburg-Leignitz." Mrs. Vanderley jumped up. "Why, Count," she said, "what ages since we met in Vienna! You remember?" "Could I ever forget? And the charming Miss Stella, she is well, I suppose not?" "Stella, you remember Count Fritz?" Stella shook hands with him. "And how is the poor, dear Prince?" asked Mrs. Vanderley. "What a terrible thing to have happened!" "I rejoice to say that my high-born master is better. He has regained consciousness and is sitting up and taking nourishment." "That's good," said old Marshall. "In a spoon only," sighed the Count. "Mr. Marshall, with your permission I should like a word with Mr. Sturgis." "Mr. Who?" The gimlet-eyed sportsman came forward. "I am Denman Sturgis, at your service." "The deuce you are! What are you doing here?" "Mr. Sturgis," explained the Count, "graciously volunteered his services - - " "I know. But what's he doing here?" "I am waiting for Mr. [COMPANION_B] Lattaker, Mr. Marshall." "Eh?" "You have not found him?" asked the Count anxiously. "Not yet, Count; but I hope to do so shortly. I know what he looks like now. This gentleman is his twin-brother. They are doubles." "You are sure this gentleman is not Mr. [COMPANION_B] Lattaker?" [COMPANION_B] put his foot down firmly on the suggestion. "Don't go mixing me up with my brother," he said. "I am Alfred. You can tell me by my mole." He exhibited the mole. He was taking no risks. The Count clicked his tongue regretfully. "I am sorry," he said. [COMPANION_B] didn't offer to console him, "Don't worry," said Sturgis. "He won't escape me. I shall find him." "Do, Mr. Sturgis, do. And quickly. Find swiftly that noble young man." "What?" shouted [COMPANION_B]. "That noble young man, [COMPANION_B] Lattaker, who, at the risk of his life, saved my high-born master from the assassin." [COMPANION_B] sat down suddenly. "I don't understand," he said feebly. "We were wrong, Mr. Sturgis," went on the Count. "We leaped to the conclusion - was it not so? - that the owner of the hat you found was also the assailant of my high-born master. We were wrong. I have heard the story from His Serene Highness's own lips. He was passing down a dark street when a ruffian in a mask sprang out upon him. Doubtless he had been followed from the Casino, where he had been winning heavily. My high-born master was taken by surprise. He was felled. But before he lost consciousness he perceived a young man in evening dress, wearing the hat you found, running swiftly towards him. The hero engaged the assassin in combat, and my high-born master remembers no more. His Serene Highness asks repeatedly, 'Where is my brave preserver?' His gratitude is princely. He seeks for this young man to reward him. Ah, you should be proud of your brother, sir!" "Thanks," said [COMPANION_B] limply. "And you, Mr. Sturgis, you must redouble your efforts. You must search the land; you must scour the sea to find [COMPANION_B] Lattaker." "He needn't take all that trouble," said a voice from the gangway. It was Voules. His face was flushed, his hat was on the back of his

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `STATUS_REVERSAL` (conf: `0.7`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [
    "STATUS_REVERSAL",
    "ESCALATION",
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 10,
  "craft_clarity": 10,
  "training_value": 10,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Long-form farce built around the invented twin identity, with repeated misunderstandings, escalating deception, status complications, and multiple reversals."
}
```

---

### Passage 021 [COMPOSITE] — *Something Fresh* (`something_fresh_ch8_10471`)

> CHAPTER VIII "'Put the butter or drippings in a kettle on the range, and when
hot add the onions and fry them; add the veal and cook until
brown. Add the water, cover closely, and cook very slowly until
the meat is tender; then add the seasoning and place the potatoes
on top of the meat. Cover and cook until the potatoes are tender,
but not falling to pieces.'" "Sure," said Mr. Peters--"not falling to pieces. That's right.
Go on." "'Then add the cream and cook five minutes longer'" read Ashe. "Is that all?" "That's all of that one." Mr. Peters settled himself more comfortably in bed. "Read me the piece where it tells about curried lobster." Ashe cleared his throat. "'Curried Lobster,'" he read. "'Materials: Two one-pound
lobsters, two teaspoonfuls lemon juice, half a spoonful curry
powder, two tablespoonfuls butter, a tablespoonful flour, one
cupful scalded milk, one cupful cracker crumbs, half teaspoonful
salt, quarter teaspoonful pepper.'" "Go on." "'Way of Preparing: Cream the butter and flour and add the
scalded milk; then add the lemon juice, curry powder, salt and
pepper. Remove the lobster meat from the shells and cut into
half-inch cubes.'" "Half-inch cubes," sighed Mr. Peters wistfully. "Yes?" "'Add the latter to the sauce.'" "You didn't say anything about the latter. Oh, I see; it means
the half-inch cubes. Yes?" "'Refill the lobster shells, cover with buttered crumbs, and bake
until the crumbs are brown. This will serve six persons.'" "And make them feel an hour afterward as though they had
swallowed a live wild cat," said Mr. Peters ruefully. "Not necessarily," said Ashe. "I could eat two portions of that
at this very minute and go off to bed and sleep like a little
child." Mr. Peters raised himself on his elbow and stared at him. They
were in the millionaire's bedroom, the time being one in the
morning, and Mr. Peters had expressed a wish that Ashe should
read him to sleep. He had voted against Ashe's novel and produced
from the recesses of his suitcase a much-thumbed cookbook. He
explained that since his digestive misfortunes had come on him he
had derived a certain solace from its perusal. It may be that to some men sorrow's crown of sorrow is
remembering happier things; but Mr. Peters had not found that to
be the case. In his hour of affliction it soothed him to read of
Hungarian Goulash and escaloped brains, and to remember that he,
too, the nut-and-grass eater of today, had once dwelt in Arcadia. The passage of the days, which had so sapped the stamina of the
efficient Baxter, had had the opposite effect on Mr. Peters. His
was one of those natures that cannot deal in half measures.
Whatever he did, he did with the same driving energy. After the
first passionate burst of resistance he had settled down into a
model pupil in Ashe's one-man school of physical culture. It had
been the same, now that he came to look back on it, at Muldoon's. Now that he remembered, he had come away from White Plains
hoping, indeed, never to see the place again, but undeniably a
different man physically. It was not the habit of Professor
Muldoon to let his patients loaf; but Mr. Peters, after the
initial plunge, had needed no driving. He had worked hard at his
cure then, because it was the job in hand. He worked hard now,
under the guidance of Ashe, because, once he had begun, the thing
interested and gripped him. Ashe, who had expected continued reluctance, had been astonished
and delighted at the way in which the millionaire had behaved.
Nature had really intended Ashe for a trainer; he identified
himself so thoroughly with his man and rejoiced at the least
signs of improvement. In Mr. Peters' case there had been distinct improvement already.
Miracles do not happen nowadays, and it was too much to expect
one who had maltreated his body so consistently for so many years
to become whole in a day; but to an optimist like Ashe signs were
not wanting that in due season Mr. Peters would rise on
stepping-stones of his dead self to higher things, and though
never soaring into the class that devours lobster a la Newburg
and smiles after it, might yet prove himself a devil of a fellow
among the mutton chops. "You're a wonder!" said Mr. Peters. "You're fresh, and you have
no respect for your elders and betters; but you deliver the
goods. That's the point. Why, I'm beginning to feel great! Say,
do you know I felt a new muscle in the small of my back this
morning? They are coming out on me like a rash." "That's the Larsen Exercises. They develop the whole body." "Well, you're a pretty good advertisement for them if they need
one. What were you before you came to me--a prize-fighter?" "That's the question everybody I have met since I arrived here
has asked me. I believe it made the butler think I was some sort
of crook when I couldn't answer it. I used to write stories--
detective stories." "What you ought to be doing is running a place over here in
England like Muldoon has back home. But you will be able to write
one more story out of this business here, if you want to. When
are you going to have another try for my scarab?" "To-night." "To-night? How about Baxter?" "I shall have to risk Baxter." Mr. Peters hesitated. He had fallen out of the habit of being
magnanimous during the past few years, for dyspepsia brooks no
divided allegiance and magnanimity has to take a back seat when
it has its grip on you. "See here," he said awkwardly; "I've been thinking this over
lately--and what's the use? It's a queer thing; and if anybody
had told me a week ago that I should be saying it I wouldn't have
believed him; but I am beginning to like you. I don't want to get
you into trouble. Let the old scarab go. What's a scarab anyway?
Forget about it and stick on here as my private Muldoon. If it's
the five thousand that's worrying you, forget that too. I'll give
it to you as your fee." Ashe was astounded. That it could really be his peppery employer
who spoke was almost unbelievable. Ashe's was a friendly nature
and he could never be long associated with anyone without trying
to establish pleasant relations; but he had resigned himself in
the present case to perpetual warfare. He was touched; and if he had ever contemplated abandoning his
venture, this, he felt, would have spurred him on to see it
through. This sudden revelation of the human in Mr. Peters was
like a trumpet call. "I wouldn't think of it," he said. "It's great of you to suggest
such a thing; but I know just how you feel about the thing, and
I'm going to get it for you if I have to wring Baxter's neck.
Probably Baxter will have given up waiting as a bad job by now if
he has been watching all this while. We've given him ten nights
to cool off. I expect he is in bed, dreaming pleasant dreams.
It's nearly two o'clock. I'll wait another ten minutes and then
go down." He picked up the cookbook. "Lie back and make yourself
comfortable, and I'll read you to sleep first." "You're a good boy," said Mr. Peters drowsily. "Are you ready? 'Pork Tenderloin Larded. Half pound fat pork--'"
A faint smile curved Mr. Peters' lips. His eyes were closed and
he breathed softly. Ashe went on in a low voice: "'four large
pork tenderloins, one cupful cracker crumbs, one cupful boiling
water, two tablespoonfuls butter, one teaspoonful salt, half
teaspoonful pepper, one teaspoonful poultry seasoning.'" A little sigh came from the bed. "'Way of Preparing: Wipe the tenderloins with a damp cloth. With
a sharp knife make a deep pocket lengthwise in each tenderloin.
Cut your pork into long thin strips and, with a needle, lard each
tenderloin. Melt the butter in the water, add the seasoning and
the cracker crumbs, combining all thoroughly. Now fill each
pocket in the tenderloin with this stuffing. Place the
tenderloins--'" A snore sounded from the pillows, punctuating the recital like a
mark of exclamation. Ashe laid down the book and peered into the
darkness beyond the rays of the bed lamp. His employer slept. Ashe switched off the light and crept to the door. Out in the
passage he stopped and listened. All was still. He stole
downstairs.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `STATUS_REVERSAL` (conf: `0.25`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [
    "DEADPAN_REACTION",
    "ESCALATION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "The passage mixes cookbook literalism, digestive misery, and escalating observations about the stomach controlling morality; the deadpan philosophical voice is central."
}
```

---

### Passage 022 [COMPOSITE] — *The Adventures Of Sally* (`the_adventures_of_sally_ch13_05083`)

> CHAPTER IV. 1872. The need of a Home further West--Burning of the Marchmont Home--Home
restored by Canadian gifts--Miss Macpherson and Miss Reavell arrive
in Canada--First visit to Knowlton in the East--Belleville Home
restored by Canadian friends--Help for the Galt Home--Miss Macpherson
returns to England--Miss Reavell remains at Galt. In her first letter on returning to England Miss Macpherson writes:-- "BELOVED FELLOW-WORKERS,--Once more at home among the old familiar
scenes in the East of London, the sadness and the sin shadows our joy
and thanksgiving. My first visit in the immediate vicinity of the
Refuge I shall not soon forget. "Taking good news of Andrew in Canada to his mother, I found his
father lying dead drunk in one corner, and his little brother lying
dead waiting to be carried off to the grave by the parish in the
other. "In the first low women's lodging-house, I found a poor misguided
girl asking me, 'How's my little sister?' "Passing on to Mr. Holland in [COMPANION_B] Yard, I cheered him with
answers to his many inquiries as to the placing out of his rescued
ones. "Many a warm shake of the hand I had from poor costermongers and
grey-headed men, for what had been done for their belongings in
taking them from the sin and want around. "My way is now open to go forward, as means permit, to rescue girls
and train them for Canada or for service in England." Miss Macpherson goes on to tell of the purchase of the Galt Home,
300 miles westward, and states the need in these words:-- "We found that to educate our Canadian family, and thoroughly fit
them to be of value to the farmer, a few fields to work upon would be
an advantage, that they might see the effects of new soil and
climate, in the growth of vegetables, shrubs, and farm produce." "Thou hast tried us as silver is tried. We went through fire and
through water, but Thou broughtest us out into a wealthy place." This
was the experience of the beginning of the year 1872. Miss
Bilbrough's letter brings to mind Deut. xxxiii. 12. "BELLEVILLE, _January 29_, 1872. "DEAREST ANNIE,--It is indeed difficult to begin a letter to you,
when I know you always open our letters feeling sure of good news.
And yet this one brings you the best you ever had. Lives spared, I
trust, to work more than ever for Him who hath done such great things
for us. Our song is one of continual thankfulness and praise, and I
know you will join us in giving thanks. Our beautiful Home lies in
ruins, only the walls standing, and there is one little grave dug by
Benjamin Stanley's, containing the ashes of little Robbie Gray. "I hardly know how to begin, it still seems so terrible and real. "We had had a happy Sabbath. We were to have an early breakfast next
morning, and I awoke in the night thinking it was daylight. Miss
Baylis came to my door, which was shut, saying, 'Miss Bilbrough,
there's smoke!' "I jumped up, and oh, the feeling, when I saw the house full of
dense white smoke! I knew well what it must be. I rushed to Mr.
Thorn's room, he was sleeping heavily, but I roused him, saying the
house was on fire; then I went down to the boys, Philips and Keen,
who were in the schoolroom, called them up and told them to save the
children, and rushed upstairs, nearly choked, calling 'Fire!' "Mrs. Wade, Miss Baylis, Miss Moore, all came out. Downstairs I ran
again and unfastened the front door, and went to the corner of the
verandah. Philips was getting out the children, and the flames were
coming on with frightful rapidity; it was blowing a perfect
hurricane, and the whole building was enveloped in smoke and ashes; I
ran back half-way upstairs to see if I could get a dress, or my
cash-box, or watch, but I was too much suffocated, and had to get back
to the front door. Mrs. Wade, Miss Baylis, and the children, were
making for the fence. I saw Mr. Thorn, and called to him to search
again with Philips for the children. "The intense cold in the snow seemed almost worse to bear than fire.
We all climbed the fence and ran to the nearest house. Poor Mrs. Wade
had got her hands frozen, even in that short time, as the thermometer
was about twelve or fifteen degrees below zero. "Here we called over the names of the children; some were here, some
in another house, sitting over the stove with bare legs and only
their little shirts on. Soon little Robbie was found missing, but
Philips had lifted him out, and he had been seen running with the
others; we suppose that the poor child, blinded with smoke, ran to
the front door, and then went through into the schoolroom, the place
he knew best, where he must soon have been suffocated. It was all
over in a few minutes, all around was fearfully bright and lurid. The
engine came, but was of course too late, the fire spread with such
terrible rapidity. "We sat almost stunned with fright and cold. Soon the Shearings and
Elliotts came, bringing clothes, &c., and we went to dear Mrs.
Elliott's house in a sleigh. It was not four A.M., and the fire was
almost out, burning round the verandah and the window-sills. "Oh, how our hearts went up in thankfulness to God for sparing
mercies! A few moments more, and we dread to think of what might have
been. Miss Baylis' door being ajar, the smoke got in; mine was shut,
my room was free, but I saw the light on the window. Miss Moore was
in Miss Lowe's bedroom; she could not realise it, and, after being
first roused, was going to bed again. "As soon as it was daylight I went with Mr. Thorn to see the ruins.
All around the melted snow had frozen like iron; the thermometer,
which was hung on the verandah, was found uninjured; nothing was
found but a table and one stove; all gone. Books, papers, clothes,
everything; but there in the blackened ruin lay distinctly the
charred frame of little Robbie. Mr. Thorn went for Dr. Holden and a
coffin, and the remains were brought to Mr. Elliott. Dear little
fellow, he was the most prepared of any of the little ones to go.
This is such a comfort to me now. "I had gathered the little ones round me in the evening before the
fire, when the others were at church, and we had sung some sweet
hymns. I made Robbie especially stand beside me, and made him sing
alone. 'I will sing for Jesus,' was the hymn he chose. He sang it
sweetly. How little did I think in a few hours he would be singing
the 'new song' before the throne! His history in our book is very
touching. 'Robert Gray, aged six; a happy little man, who can say
little or nothing about himself.' The rest of the page is blank, as
he had never been away from Marchmont. An inquest was held over the
body. We wished it especially, so that we might have an investigation
as to the cause of the fire. "Dearest Annie, when I think what it might have been, and the grief
of all at home, and the intense sorrow, oh, it makes one so thankful!
I felt Jesus very precious through it all, recognising His hand in so
many ways. I had had much blessed communion with Him that Sunday, and
several seasons of sweet prayer. I can fully realise that for me it
would have been all right, if the Lord had ordered it otherwise; but
for the sake of those at home I bless God for life spared, and trust
earnestly the Lord may give us all increased power and spiritual
life. Having passed through 'the fire,' may we also receive the
baptism of the Holy Ghost. And oh, may our lives be more and more
devoted to His service! Not our own, but bought with a price, may we
live more and more unto Him who hath loved us! "Miss Moore was out at nine o'clock in the woodshed; all was safe
then. Mrs. Wade locked the doors at ten with stable lantern in the
wood-shed (the boys' summer dining-room), and then all was safe; the
fire in the kitchen stove was out. She came shivering in to-prayers a
little after ten. The parlour fire was nearly out, and Miss Baylis
and I were quite cold. The fire upstairs was not lit, nor had any
ashes been taken up on Sunday morning. If any had been removed on
Saturday, they were placed in iron vessels in the first kitchen. The
fire broke out in the further corner of the wood-shed. The cause is
so far quite unknown, and will, I suppose, ever remain so. "I send you the account of the inquest, and other papers, as I know
well it is better to see and know all particulars. I cannot, however,
tell of all the kindness and sympathy we have met with--a telegram
from Mr. Claxton, offering money, &c., Hon. [COMPANION_B] Alien wishing to
take the children; Mr. Eason: 'I am praying for you, can I help by
coming?' numbers of friends coming with clothes of every kind;
subscriptions got up to start a new Home immediately; sewing
societies at work and ladies canvassing the town in every direction
for help to furnish another Home at once. I could not even begin to
particularise our friends. Mr. Flint came up at eight, begging me to
come to his house. "This afternoon we have buried little Robin. The service was held in
Mr. Elliott's church. "How often we have thought of home friends during the last few days,
and longed that you might not hear the news in any way till this
reaches you, which will be nearly three weeks! and now you must fancy
us happy at our work again, and as much under the loving care and
protection of our God as ever, trusting only to Him for everything,
that whether absent from the body, or still in the flesh, we may be
more and more filled with faith and love for the Lord's work. "Wednesday. We seem each day to realise only more fully our
marvellous escape. The firemen say they never remember such a night,
nor saw a house burn so rapidly. Now every one is so kind; things
keep pouring in for the new Home;--it is to be Canadian this time,
not English. Mr. Flint says he has written to you, telling you all,
but he could not tell you one quarter of the kindness we have met
with on every hand. "Oh, that verse in Isa. lxiv. II, is so expressive: "'Our beautiful house where we praised Thee is burnt up with fire,
and all our pleasant things are laid waste.' What a ruin Marchmont is
now! the blackened ashes all around--nothing but the walls standing.
I feel such mingled feelings as I look at it--all the happy days we
have spent there--the holy associations never to return again. "'We have no continuing city here,' was the text which filled Mr.
Thorn's mind, and it is one we hope more than ever to keep before us.
This trial seems to have given the four of us deeper sympathy and
interest together. So nearly entering eternity together, and yet
saved, we trust, to render more devoted service to the Master, for
having passed through this fiery trial. "I can hardly bear to think of all the sorrow you are feeling for
us; but oh! let thanksgiving and praise be uppermost. It is the one
thought that fills our minds. We are wonderful in health, no cold,
and are as occupied as possible, looking after the children, and
preparing for the new Home. Happily, Charlie the horse, the sleigh,
and the buffalo robes are safe, and most useful we find them now. "I am so thankful that it will be nearly three weeks ere you know,
and you must think of it as past and gone, and, if possible, just at
first see the beginning of great good in making the work more known,
and rousing the sympathies of others." What, Marchmont gone!
  That pleasant Home nought but a memory now;
  And yet, in humble thankfulness we bow,--
      Father, Thy will be done. It was but lent:
  Thou wilt not that Thy children fix their heart
  On aught below: theirs is a better part--
      A treasury unspent. Still are its memories dear!
  The maple shadows that around it lay,
  Stirred by the breezes from the silvery bay,
      Or bathed in moonlight clear-- How fair were they!
  Lovely when decked with earliest buds of spring,
  Loveliest when radiant autumn came to fling
      A glory on each spray. Oh home of praise and prayer!
  Where glad sweet voices raised the morning hymn,
  Pleaded for blessing in the twilight dim,
      Or thrilled the midnight air. Can we forget
  The meetings and the partings we have known?
  The welcome glad, the farewell's sadder tone--
      Ah, we remember yet. We were not there
  When thro' its halls the fierce destroyer swept;
  But God was watching, while our dear ones slept--
      Safe were they in His care. All safe with Him;
  Yes, for our Robbie "sings for Jesus" now
  In sweeter tones, with far more sunny brow,
      And eyes no tear's can dim. They wait His word--
  Stanley and Robbie side by side--and we
  Caught up together with them soon shall be
      For ever with the Lord. S. R. GELDARD. All former kindness was as nothing compared to that now received, as
will be seen by the following from Miss Bilbrough:-- "BELLEVILLE, _February 2, 1872_. "I know that many many prayers are now being offered for us, and
that the Lord is answering them every minute, giving us sustaining
grace and wisdom, and help as to the future. I knew it would be five
weeks before I could hear from you, and I could trust that all we
might arrange here would meet your approval, as it has generally done. "However, the Belleville people, with Mr. Flint at their head, quite
took the matter out of my hand, being determined that they would
provide and furnish themselves a still better house than Marchmont.
The sympathy awakened is great, and the pleasure of friends at
hearing that we could have a large substantial house on the Kingston
Road for our orphan children was equally so. Mr. Flint has secured it
for three years, the Council paying the rent and taxes, and
sufficient is already gathered to furnish it. So that when the first
arrivals come in May, all will be ready for them. "How good the Lord is! even out of apparent trial He brings the
good. We had been praying for special blessing, and in this way,
(strange as it seems to us), we do recognise the answer." In March, Miss Macpherson writes:-- "BELOVED FRIENDS,--While you are reading this, my pathway will again
be upon the mighty deep. The Lord willing, I look to leave Liverpool
by steam-ship 'Scandinavian,' March 7th. Miss Reavell, who has for
two years been our scribe in the Refuge, accompanies me. Your prayers
have gone up that blessing may be ours, as a little band of feeble
workers for our Lord, and if He has been pleased to try our faith by
the trial of fire, shall we not praise Him for anything His loving
hand doth send us? And as one has beautifully said, 'What God takes
it is always gain to lose.' Heaven is nearer now our little Robbie is
there; Jesus is dearer, and has quickened us all by His constraining
love. "My object in going now to Canada without children is twofold.
Strength being given, my desire is to visit the new districts, where
I hope in the coming summer to place out the hundreds now under
excellent training and holy influence here and in Scotland, and to
find out Christian families who may be willing to receive them on
arrival. Plead that the Holy Spirit may fill with power those who are
daily seeking to win these wanderers back to the fold. "Secondly, I wish to make use of the late sad calamity, and God's
wonderful interposition in saving life, so that the teaching may not
be lost upon the hundreds of immortal souls connected with our
mission." It is impossible to describe the eagerness with which the arrival of
these dear friends was looked for, and day after day, those in
service in and around Belleville would come with the hope of seeing
them. And among these were former match-box makers, who had been
rescued from such depths of sorrow; one of whom had already saved
from her wages sufficient to pay her brother's passage out, besides
bringing offerings of her own work towards the furnishing of Miss
Macpherson's room in the new House. Through many dangers they were
brought safely, in answer to many prayers, but Miss Reavell had
suffered much on the voyage, and one special instance of the Lord's
care I cannot help here recording, "They shall abundantly utter the
memory of Thy great goodness." Miss Reavell had been a most diligent
and necessary labourer at the Home of Industry night and day. At sea
her strength seemed to fail; she only existed on oranges, and the
last orange was gone. In the midst of a fearful storm, signals were
made by another vessel that they were without food, and the life-boat
was put off from the steamer, carrying to the distressed vessel a
barrel of flour and pork In return, a thank-offering came in the
shape of two boxes of the best oranges, the ship being from Palermo,
bound for New York with a cargo of fruit. "Even the very hairs of
your head are all numbered." The visit of Miss Barber, a Canadian lady of influence, to the Home
of Industry, was the means of interesting friends in the Eastern
Townships' Province of Quebec, and of leading them to open a Home at
Knowlton. The following letter is from Miss Macpherson:-- "The year's experiment in this new district will enable us to test it
as to whether it will be a suitable one for our children; if so, it
will not cost many pounds of English money. The old house we have
taken was formerly a tavern, and its ball-room will make us an
excellent dormitory; the rent is only 20 pounds, and is paid entirely
by a Canadian. Should the children thrive under the fostering care of
our dear friend Miss Barber (now doubly dear to us all after the
winter of help she has given us in the East of London), there will be
no difficulty in establishing a permanent Home, built of brick, half
of the necessary sum having already been subscribed in and around
Sheffield, Leeds, and Nottingham; and the other half our friends in
the province of Quebec have freely offered to collect. Thus will those
both on this side and at home share the benefits; the old country
seeing hundreds educated that might otherwise in a few years become
expensive criminals, and the new country, receiving, ere habits are
fixed, young life which, in future, will call Canada 'the home of its
adoption.' "Though, according to all accounts, this is an uncommonly heavy
snow-season, I have no fears for the children, the air is so dry and
clear, and well fitted to invigorate their frames. This morning I
started about five o'clock, and soon forgot the fear which had crept
over me but a week ago, when I took my first winter journey among
these snowy hills. 'Knowledge is power,' and the experience of dangers
met and passed gives quietness and confidence. "You will be imagining that owing to these prolonged snow-storms all
work is stayed. Not so; everything goes on most vigorously--lumbering,
carting, cutting wood for summer's need. Ladies seem
always busy; yet as it is often seen, those who have most to do can
best arrange to be at leisure. There is an education of forethought
caused by having to watch against the heat and cold; this has deeply
interested me in the practical manner in which they are going to work
in furnishing this Eastern Townships' Home. In return for the
kindness shown to this Mission, may the whole district be spiritually
blessed, and may our loving Lord be the joy and strength of each
faithful labourer! "The heavy calamity that it pleased our Father to send by fire, has
accomplished in a few weeks that which would otherwise, humanly
speaking, have taken many years to make known. Our motives and
principles of service were all new, and even our simple faith and
trust in prayer were often misunderstood. Though we had travelled
several thousands of miles in Canada, seeking to stir up Christians
to aid us in finding and watching over the right home for our
children, we had no medium on this side like 'The Christian,' by
which we could communicate with those like-minded, and tell them of
our burdens. "The Hon. B. Flint tells us how the hearts of his fellow-townsmen
were moved with compassion on hearing of the destruction of the
Children's Home, on that terrible night, and that some of them
attempted to ascend the hill and offer aid, but had to turn back,
unable to face the hurricane and tempest. "The citizens of Belleville have contributed freely towards
replacing the Home, and the Lord's dear children all over the land
have sent their love-offerings. The County Council received
testimonies from many of the homesteads concerning the six hundred
children placed out round Belleville, and generously contributed 500
dollars to show their esteem for the work. The funds in hand led Mr.
Flint, after the withdrawal of the rented house at first proposed, to
purchase a freehold of three and a quarter acres, possessing a good
house and out-buildings, which were adapted to our use by the
addition of dormitories, and furnished by the aid of the ladies of
Belleville. This Home is now given to us for so long as it shall be
used by our mission band in connection with the emigration of
children to this district." In April, a detachment of thirty elder boys arrived, to be followed
quickly by others. In June 1872, when 150 emigrants arrived, 50 children were sent to
each of the three Homes now opened to receive them, and for several
years this order was observed, until other arrangements were made to
meet the growing character of the work. The following tells of the progress of the Galt Home:-- "Many will wish to know how this Home at Galt shapes itself, and
would be amused at the varied occupations of the past week. "A Canadian springtime is very brief, so we have had to buy a span
of horses and a plough, and, with the aid of other neighbours'
ploughs, the corn and clover seed will soon be all sown. The ladies
of several churches have met in the council-chamber, and worked at
all household gear, others superintending the house arrangements, and
purchasing necessary things. "My part has been that of a faithful recipient, giving praise from
hour to hour to Him who hath laid my every burden here on His own
children's hearts. The past little season has been to me a precious
rest-time, seeing others work. We expect to be all in order by the
arrival of our next party. The threshing-floor we have transformed
into a dining-room; one of the barns is fitted up as a dormitory. The
chaff-house makes a lavatory; and, from the interest around, we do
not expect to keep our little men very long out of the homes waiting
for them. "The love-tokens here, as at home, are varied in their character.
Our farmer's wife has set us up with poultry, another with eggs; a
little boy brought us his pet hen as an offering; indeed, wherever we
turn, some kind thought is shown, and our hearts are gladdened, and
our faith is able to rejoice at the prospect of returning home, and
gathering up another thousand precious young immortals from the
depths of our sin-stricken cities, and placing them out in homes
where Jesus is loved." In June, Miss Macpherson was welcomed back with warm thanksgivings,
having left the Home at Galt under the wise and loving care of her
faithful companion, Miss Reavell. In after years Mr. and Mrs. Merry
devoted themselves chiefly to this branch of the work, and have been
the watchful and tender foster parents of this ever-varying family.
It would be hard to say whether Mrs. Merry's presence was more valued
here, or among the sorrowful widowed mothers in Spitalfields.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `ESCALATION` (conf: `0.98`)
- **Temporal Horizon:** `LOCAL` | Secondary: `['DIALOGUE_SUBTEXT']`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 5,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Serious missionary history, fire, death, grief, and religious reflection dominate; not comedy craft."
}
```

---

### Passage 023 [COMPOSITE] — *The Diary Of A Nobody* (`the_diary_of_a_nobody_ch1_03005`)

> "impossible to avoid the conclusion, first, that either this writer was gifted with faculties passing all human experience, or else his knowledge was divine," Gladstone argues that the fact of this coincidence of the pentateuchal story with the results of modern investigation makes it And having settled to his own satisfaction that the first "branch of the alternative is truly nominal and unreal," Mr.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 6,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Historical/religious argument rather than a comic scene or transferable comic mechanism."
}
```

---

### Passage 024 [COMPOSITE] — *The Inimitable Jeeves* (`the_inimitable_jeeves_ch37_04501`)

> "and that," " Indeed, Clough got
quite excited over the thought that London, of all cities in the world,
possessed no decent accommodation for merchants transacting their everyday
business, and declared his readiness to build "so fere a bourse in London
as the grett bourse is in Andwarpe withhoutt molestyng of any
man more than he shulld be well dysposyd to geve.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 5,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Historical exposition about a London bourse; no self-contained comic engine."
}
```

---

### Passage 025 [COMPOSITE] — *The Little Nugget* (`the_little_nugget_ch1_09379`)

> "Now what do thim clerks be wantin' to know, I wonder! 'Prisint condition, 'is ut? Thim pigs, praise St. Patrick, do be in good health, so far as I know, but I niver was no veternairy surgeon to dago pigs. Mebby thim clerks wants me to call in the pig docther an' have their pulses took. Wan thing I do know, howiver, which is they've glorious appytites for pigs of their soize. Ate? They'd ate the brass padlocks off of a barn door I If the paddy pig, by the same token, ate as hearty as these dago pigs do, there'd be a famine in Ireland," To assure himself that his report would be up to date, Flannery went to the rear of the office and looked into the cage.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 8,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Flannery's attempt to satisfy bureaucratic reporting requirements becomes increasingly absurd through exaggerated descriptions of the pigs' appetites."
}
```

---

### Passage 026 [COMPOSITE] — *The Man Upstairs* (`the_man_upstairs_ch41_02243`)

> "here has been my bailiff to inform me of the loss of four of the choicest ewes out of that little flock of Southdowns I set such store by, and which arrived in the north but two months since. And the poor creatures have been destroyed in so strange a manner, for their carcasses are horribly mangled," "A strange story I have just been told," said he; Most of us uttered some expression of pity or surprise, and some suggested that a vicious dog was probably the culprit.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 6,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Loss of sheep and mangled carcasses are presented as a serious mystery; the excerpt does not establish comedy craft."
}
```

---

### Passage 027 [COMPOSITE] — *Their Mutual Child* (`their_mutual_child_ch13_01342`)

> "said Mr. Gladstone," "I
always hold, that politicians are the men whom,
as a rule, it is most difficult to comprehend"; and he added, by way of
strengthening it: "For my own part, I never have thus understood, or
thought I understood, above one or two.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 7,
  "craft_clarity": 7,
  "training_value": 6,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "A compact paradoxical joke: politicians are said to be difficult to comprehend, followed by the speaker admitting he has comprehended almost none of them."
}
```

---

### Passage 028 [COMPOSITE] — *Three Men In A Boat* (`three_men_in_a_boat_ch12_02913`)

> Speaker: Character | Target Emotion: Fearful
"because they are the only two inns in the place," "Well, I don't know what you'll do, I'm sure," said our informant;.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "PARTIAL",
  "craft_stratum": "REJECT",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 6,
  "craft_clarity": 4,
  "training_value": 4,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "The line becomes comic in context because there are only two inns, but the supplied excerpt does not contain enough of the setup or payoff."
}
```

---

### Passage 029 [COMPOSITE] — *Three Men On The Bummel* (`three_men_on_the_bummel_ch11_05815`)

> "Don't you think," said [COMPANION_B], "that if we made our way back to the
village, and hired a boy for a mark to guide us, it would save time in
the end?".

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "PARTIAL",
  "craft_stratum": "REJECT",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 6,
  "craft_clarity": 4,
  "training_value": 4,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "A plausible comic suggestion, but there is no developed reversal or payoff in the isolated sentence."
}
```

---

### Passage 030 [COMPOSITE] — *A Damsel In Distress* (`a_damsel_in_distress_ch8_00421`)

> "One of these days," said Jimmy plaintively, "I shall be sitting
by the roadside with my dinner-pail, and you will come by in your
limousine, and I shall look up at you and say '_You_ hounded me
into this!' How will you feel then?".

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [
    "STATUS_REVERSAL"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 8,
  "craft_clarity": 7,
  "training_value": 7,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Jimmy invents a deliberately melodramatic future in which their social positions are reversed; the absurdly specific image is the comic device."
}
```

---

### Passage 031 [COMPOSITE] — *Love Among The Chickens* (`love_among_the_chickens_ch25_08563`)

> Speaker: Tanya | Target Emotion: Urgent / Cautious
"And I, Musechka," said Tanya Kovalchuk mournfully, "must I go alone?
We lived together, and now - ".

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 6,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Mournful emotional dialogue with no clear comic mechanism in the supplied passage."
}
```

---

### Passage 032 [COMPOSITE] — *My Man Jeeves* (`my_man_jeeves_ch1_06305`)

> "I fancy it would be a simple matter, sir, to find some impecunious author who would be glad to do the actual composition of the volume for a small fee. It is only necessary that the young lady's name should appear on the title page," "That's true," said [FRIEND].

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "PARTIAL",
  "craft_stratum": "REJECT",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": true,
  "literary_quality": 7,
  "craft_clarity": 5,
  "training_value": 5,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "The ghostwriting proposal has dry comic potential, but this excerpt is primarily setup and does not provide enough of the comic sequence."
}
```

---

### Passage 033 [COMPOSITE] — *Right Ho* (`right_ho_ch2_00549`)

> "I wish you would try to knock a little sense into him and make him quit this playing at painting. But I have an idea that he is steadying down. I noticed it first that night he came to dinner with us, my dear, to be introduced to you. He seemed altogether quieter and more serious. Something seemed to have sobered him. Perhaps you will give us the pleasure of your company at dinner to-night, Mr. [PROTAGONIST]? Or have you dined?," I said I had.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 6,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Ordinary social conversation about a man's behavior and dinner; no sufficiently clear comic engine."
}
```

---

### Passage 034 [COMPOSITE] — *Something Fresh* (`something_fresh_ch9_03926`)

> Speaker: In | Target Emotion: Hopeful / Reassuring
"what do you imagine you are doing?," "In the name of goodness, Frederick," said Lord Emsworth
peevishly,.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "PARTIAL",
  "craft_stratum": "REJECT",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 6,
  "craft_clarity": 3,
  "training_value": 3,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "The exchange may be comic in the larger scene, but the isolated lines do not establish the mechanism."
}
```

---

### Passage 035 [COMPOSITE] — *The Diary Of A Nobody* (`the_diary_of_a_nobody_ch3_07357`)

> "first or cosmogonical portion of the Proem not only accords with, but teaches, the nebular hypothesis," Gladstone informs us that Professor Dana and Professor Guyot are prepared to prove that the There is no one to whose authority on geological questions I am more readily disposed to bow than that of my eminent friend Professor Dana.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 4,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Technical/historical exposition with no comic craft."
}
```

---

### Passage 036 [COMPOSITE] — *The Inimitable Jeeves* (`the_inimitable_jeeves_ch44_02680`)

> "the hand and the place," This "very antient memorandum" of the Lord
      Mayor's precedence in the City was submitted to Charles II in 1670,
      when that monarch insisted upon Sir Richard Ford, the Lord Mayor of
      the day, giving to the Prince of Orange
      (afterwards William III of England), on the occasion of the prince
      being entertained by the City.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 5,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Historical editorial exposition about civic precedence; no self-contained comedy."
}
```

---

### Passage 037 [COMPOSITE] — *The Little Nugget* (`the_little_nugget_ch2_05175`)

> "Rules may be rules, but you can't fool Mike Flannery twice wid the same thrick--whin ut comes to live stock, dang the rules. So long as Flannery runs this expriss office--pigs is pets--an' cows is pets--an' horses is pets--an' lions an' tigers an' Rocky Mountain goats is pets--an' the rate on thim is twinty-foive cints," He paused long enough to let one of the boys put an empty basket in the place of the one he had just filled.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `ESCALATION` (conf: `0.25`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": true,
  "notes": "The repeated list—pigs, cows, horses, then lions and tigers—extends the absurd rule through escalating examples; rhythm and dialect amplify the joke."
}
```

---

### Passage 038 [COMPOSITE] — *The Man Upstairs* (`the_man_upstairs_ch15_01091`)

> "Well, Jup," said I, "what is the matter now? - how is your master?" "Why, to speak the troof, massa, him not so berry well as mought be.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "PARTIAL",
  "craft_stratum": "REJECT",
  "primary_mechanism": "DEADPAN_REACTION",
  "secondary_mechanisms": [
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": true,
  "literary_quality": 6,
  "craft_clarity": 4,
  "training_value": 4,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "The reply may be an understated comic line, but the fragment alone does not establish enough setup or payoff."
}
```

---

### Passage 039 [COMPOSITE] — *Their Mutual Child* (`their_mutual_child_ch11_00603`)

> "C'est une peau de rhinocere!," No one got back on him with a
blow equally mischievous--not even the Queen--for, as old Baron Brunnow
described him: Having gained his point,
he laughed, and his public laughed with him, for the usual British--or
American--public likes to be amused, and thought it very amusing to see
these beribboned and bestarred foreigners caught and tossed and gored
on the horns of this jovial, slashing, devil-may-care British bull.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "PARTIAL",
  "craft_stratum": "REJECT",
  "primary_mechanism": "STATUS_REVERSAL",
  "secondary_mechanisms": [
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 7,
  "craft_clarity": 5,
  "training_value": 4,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "The passage describes a public figure verbally defeating decorated foreigners and clearly has comic rhetoric, but it is not a clean local craft example."
}
```

---

### Passage 040 [COMPOSITE] — *Three Men In A Boat* (`three_men_in_a_boat_ch4_09172`)

> "We shan't want any tea," said [COMPANION_B] ([COMPANION_A]'s face fell at this);
"but we'll have a good round, square, slap-up meal at seven - dinner,
tea, and supper combined.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [
    "MISUNDERSTANDING",
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 8,
  "craft_clarity": 8,
  "training_value": 8,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "The apparent cancellation of tea is immediately contradicted by ordering dinner, tea, and supper as one meal; the comic force comes from deadpan literal phrasing."
}
```

---

### Passage 041 [COMPOSITE] — *Three Men On The Bummel* (`three_men_on_the_bummel_ch7_00956`)

> CHAPTER VII [COMPANION_B] wonders--German love of order--"The Band of the Schwarzwald
Blackbirds will perform at seven"--The china dog--Its superiority over
all other dogs--The German and the solar system--A tidy country--The
mountain valley as it ought to be, according to the German idea--How the
waters come down in Germany--The scandal of Dresden--[COMPANION_A] gives an
entertainment--It is unappreciated--[COMPANION_B] and the aunt of him--[COMPANION_B], a
cushion, and three damsels. At a point between Berlin and Dresden, [COMPANION_B], who had, for the last
quarter of an hour or so, been looking very attentively out of the
window, said: "Why, in Germany, is it the custom to put the letter-box up a tree? Why
do they not fix it to the front door as we do? I should hate having to
climb up a tree to get my letters. Besides, it is not fair to the
postman. In addition to being most exhausting, the delivery of letters
must to a heavy man, on windy nights, be positively dangerous work. If
they will fix it to a tree, why not fix it lower down, why always among
the topmost branches? But, maybe, I am misjudging the country," he
continued, a new idea occurring to him. "Possibly the Germans, who are
in many matters ahead of us, have perfected a pigeon post. Even so, I
cannot help thinking they would have been wiser to train the birds, while
they were about it, to deliver the letters nearer the ground. Getting
your letters out of those boxes must be tricky work even to the average
middle-aged German." I followed his gaze out of window. I said: "Those are not letter-boxes, they are birds' nests. You must understand
this nation. The German loves birds, but he likes tidy birds. A bird
left to himself builds his nest just anywhere. It is not a pretty
object, according to the German notion of prettiness. There is not a bit
of paint on it anywhere, not a plaster image all round, not even a flag.
The nest finished, the bird proceeds to live outside it. He drops things
on the grass; twigs, ends of worms, all sorts of things. He is
indelicate. He makes love, quarrels with his wife, and feeds the
children quite in public. The German householder is shocked. He says to
the bird: "'For many things I like you. I like to look at you. I like to hear you
sing. But I don't like your ways. Take this little box, and put your
rubbish inside where I can't see it. Come out when you want to sing; but
let your domestic arrangements be confined to the interior. Keep to the
box, and don't make the garden untidy.'" In Germany one breathes in love of order with the air, in Germany the
babies beat time with their rattles, and the German bird has come to
prefer the box, and to regard with contempt the few uncivilised outcasts
who continue to build their nests in trees and hedges. In course of time
every German bird, one is confident, will have his proper place in a full
chorus. This promiscuous and desultory warbling of his must, one feels,
be irritating to the precise German mind; there is no method in it. The
music-loving German will organise him. Some stout bird with a specially
well-developed crop will be trained to conduct him, and, instead of
wasting himself in a wood at four o'clock in the morning, he will, at the
advertised time, sing in a beer garden, accompanied by a piano. Things
are drifting that way. Your German likes nature, but his idea of nature is a glorified Welsh
Harp. He takes great interest in his garden. He plants seven rose trees
on the north side and seven on the south, and if they do not grow up all
the same size and shape it worries him so that he cannot sleep of nights.
Every flower he ties to a stick. This interferes with his view of the
flower, but he has the satisfaction of knowing it is there, and that it
is behaving itself. The lake is lined with zinc, and once a week he
takes it up, carries it into the kitchen, and scours it. In the
geometrical centre of the grass plot, which is sometimes as large as a
tablecloth and is generally railed round, he places a china dog. The
Germans are very fond of dogs, but as a rule they prefer them of china.
The china dog never digs holes in the lawn to bury bones, and never
scatters a flower-bed to the winds with his hind legs. From the German
point of view, he is the ideal dog. He stops where you put him, and he
is never where you do not want him. You can have him perfect in all
points, according to the latest requirements of the Kennel Club; or you
can indulge your own fancy and have something unique. You are not, as
with other dogs, limited to breed. In china, you can have a blue dog or
a pink dog. For a little extra, you can have a double-headed dog. On a certain fixed date in the autumn the German stakes his flowers and
bushes to the earth, and covers them with Chinese matting; and on a
certain fixed date in the spring he uncovers them, and stands them up
again. If it happens to be an exceptionally fine autumn, or an
exceptionally late spring, so much the worse for the unfortunate
vegetable. No true German would allow his arrangements to be interfered
with by so unruly a thing as the solar system. Unable to regulate the
weather, he ignores it. Among trees, your German's favourite is the poplar. Other disorderly
nations may sing the charms of the rugged oak, the spreading chestnut, or
the waving elm. To the German all such, with their wilful, untidy ways,
are eyesores. The poplar grows where it is planted, and how it is
planted. It has no improper rugged ideas of its own. It does not want
to wave or to spread itself. It just grows straight and upright as a
German tree should grow; and so gradually the German is rooting out all
other trees, and replacing them with poplars. Your German likes the country, but he prefers it as the lady thought she
would the noble savage--more dressed. He likes his walk through the
wood--to a restaurant. But the pathway must not be too steep, it must
have a brick gutter running down one side of it to drain it, and every
twenty yards or so it must have its seat on which he can rest and mop his
brow; for your German would no more think of sitting on the grass than
would an English bishop dream of rolling down One Tree Hill. He likes
his view from the summit of the hill, but he likes to find there a stone
tablet telling him what to look at, find a table and bench at which he
can sit to partake of the frugal beer and "belegte Semmel" he has been
careful to bring with him. If, in addition, he can find a police notice
posted on a tree, forbidding him to do something or other, that gives him
an extra sense of comfort and security. Your German is not averse even to wild scenery, provided it be not too
wild. But if he consider it too savage, he sets to work to tame it. I
remember, in the neighbourhood of Dresden, discovering a picturesque and
narrow valley leading down towards the Elbe. The winding roadway ran
beside a mountain torrent, which for a mile or so fretted and foamed over
rocks and boulders between wood-covered banks. I followed it enchanted
until, turning a corner, I suddenly came across a gang of eighty or a
hundred workmen. They were busy tidying up that valley, and making that
stream respectable. All the stones that were impeding the course of the
water they were carefully picking out and carting away. The bank on
either side they were bricking up and cementing. The overhanging trees
and bushes, the tangled vines and creepers they were rooting up and
trimming down. A little further I came upon the finished work--the
mountain valley as it ought to be, according to German ideas. The water,
now a broad, sluggish stream, flowed over a level, gravelly bed, between
two walls crowned with stone coping. At every hundred yards it gently
descended down three shallow wooden platforms. For a space on either
side the ground had been cleared, and at regular intervals young poplars
planted. Each sapling was protected by a shield of wickerwork and bossed
by an iron rod. In the course of a couple of years it is the hope of the
local council to have "finished" that valley throughout its entire
length, and made it fit for a tidy-minded lover of German nature to walk
in. There will be a seat every fifty yards, a police notice every
hundred, and a restaurant every half-mile. They are doing the same from the Memel to the Rhine. They are just
tidying up the country. I remember well the Wehrthal. It was once the
most romantic ravine to be found in the Black Forest. The last time I
walked down it some hundreds of Italian workmen were encamped there hard
at work, training the wild little Wehr the way it should go, bricking the
banks for it here, blasting the rocks for it there, making cement steps
for it down which it can travel soberly and without fuss. For in Germany there is no nonsense talked about untrammelled nature. In
Germany nature has got to behave herself, and not set a bad example to
the children. A German poet, noticing waters coming down as Southey
describes, somewhat inexactly, the waters coming down at Lodore, would be
too shocked to stop and write alliterative verse about them. He would
hurry away, and at once report them to the police. Then their foaming
and their shrieking would be of short duration. "Now then, now then, what's all this about?" the voice of German
authority would say severely to the waters. "We can't have this sort of
thing, you know. Come down quietly, can't you? Where do you think you
are?" And the local German council would provide those waters with zinc pipes
and wooden troughs, and a corkscrew staircase, and show them how to come
down sensibly, in the German manner. It is a tidy land is Germany. We reached Dresden on the Wednesday evening, and stayed there over the
Sunday. Taking one consideration with another, Dresden, perhaps, is the most
attractive town in Germany; but it is a place to be lived in for a while
rather than visited. Its museums and galleries, its palaces and gardens,
its beautiful and historically rich environment, provide pleasure for a
winter, but bewilder for a week. It has not the gaiety of Paris or
Vienna, which quickly palls; its charms are more solidly German, and more
lasting. It is the Mecca of the musician. For five shillings, in
Dresden, you can purchase a stall at the opera house, together,
unfortunately, with a strong disinclination ever again to take the
trouble of sitting out a performance in any English, French, or American
opera house. The chief scandal of Dresden still centres round August the Strong, "the
Man of Sin," as Carlyle always called him, who is popularly reputed to
have cursed Europe with over a thousand children. Castles where he
imprisoned this discarded mistress or that--one of them, who persisted in
her claim to a better title, for forty years, it is said, poor lady! The
narrow rooms where she ate her heart out and died are still shown.
Chateaux, shameful for this deed of infamy or that, lie scattered round
the neighbourhood like bones about a battlefield; and most of your
guide's stories are such as the "young person" educated in Germany had
best not hear. His life-sized portrait hangs in the fine Zwinger, which
he built as an arena for his wild beast fights when the people grew tired
of them in the market-place; a beetle-browed, frankly animal man, but
with the culture and taste that so often wait upon animalism. Modern
Dresden undoubtedly owes much to him. But what the stranger in Dresden stares at most is, perhaps, its electric
trams. These huge vehicles flash through the streets at from ten to
twenty miles an hour, taking curves and corners after the manner of an
Irish car driver. Everybody travels by them, excepting only officers in
uniform, who must not. Ladies in evening dress, going to ball or opera,
porters with their baskets, sit side by side. They are all-important in
the streets, and everything and everybody makes haste to get out of their
way. If you do not get out of their way, and you still happen to be
alive when picked up, then on your recovery you are fined for having been
in their way. This teaches you to be wary of them. One afternoon [COMPANION_A] took a "bummel" by himself. In the evening, as we
sat listening to the band at the Belvedere, [COMPANION_A] said, _a propos_ of
nothing in particular, "These Germans have no sense of humour." "What makes you think that?" I asked. "Why, this afternoon," he answered, "I jumped on one of those electric
tramcars. I wanted to see the town, so I stood outside on the little
platform--what do you call it?" "The Stehplatz," I suggested. "That's it," said [COMPANION_A]. "Well, you know the way they shake you about,
and how you have to look out for the corners, and mind yourself when they
stop and when they start?" I nodded. "There were about half a dozen of us standing there," he continued, "and,
of course, I am not experienced. The thing started suddenly, and that
jerked me backwards. I fell against a stout gentleman, just behind me.
He could not have been standing very firmly himself, and he, in his turn,
fell back against a boy who was carrying a trumpet in a green baize case.
They never smiled, neither the man nor the boy with the trumpet; they
just stood there and looked sulky. I was going to say I was sorry, but
before I could get the words out the tram eased up, for some reason or
other, and that, of course, shot me forward again, and I butted into a
white-haired old chap, who looked to me like a professor. Well, _he_
never smiled, never moved a muscle." "Maybe, he was thinking of something else," I suggested. "That could not have been the case with them all," replied [COMPANION_A], "and
in the course of that journey, I must have fallen against every one of
them at least three times. You see," explained [COMPANION_A], "they knew when
the corners were coming, and in which direction to brace themselves. I,
as a stranger, was naturally at a disadvantage. The way I rolled and
staggered about that platform, clutching wildly now at this man and now
at that, must have been really comic. I don't say it was high-class
humour, but it would have amused most people. Those Germans seemed to
see no fun in it whatever--just seemed anxious, that was all. There was
one man, a little man, who stood with his back against the brake; I fell
against him five times, I counted them. You would have expected the
fifth time would have dragged a laugh out of him, but it didn't; he
merely looked tired. They are a dull lot." [COMPANION_B] also had an adventure at Dresden. There was a shop near the
Altmarkt, in the window of which were exhibited some cushions for sale.
The proper business of the shop was handling of glass and china; the
cushions appeared to be in the nature of an experiment. They were very
beautiful cushions, hand-embroidered on satin. We often passed the shop,
and every time [COMPANION_B] paused and examined those cushions. He said he
thought his aunt would like one. [COMPANION_B] has been very attentive to this aunt of his during the journey. He
has written her quite a long letter every day, and from every town we
stop at he sends her off a present. To my mind, he is overdoing the
business, and more than once I have expostulated with him. His aunt will
be meeting other aunts, and talking to them; the whole class will become
disorganised and unruly. As a nephew, I object to the impossible
standard that [COMPANION_B] is setting up. But he will not listen. Therefore it was that on the Saturday he left us after lunch, saying he
would go round to that shop and get one of those cushions for his aunt.
He said he would not be long, and suggested our waiting for him. We waited for what seemed to me rather a long time. When he rejoined us
he was empty handed, and looked worried. We asked him where his cushion
was. He said he hadn't got a cushion, said he had changed his mind, said
he didn't think his aunt would care for a cushion. Evidently something
was amiss. We tried to get at the bottom of it, but he was not
communicative. Indeed, his answers after our twentieth question or
thereabouts became quite short. In the evening, however, when he and I happened to be alone, he broached
the subject himself. He said: "They are somewhat peculiar in some things, these Germans." I said: "What has happened?" "Well," he answered, "there was that cushion I wanted." "For your aunt," I remarked. "Why not?" he returned. He was huffy in a moment; I never knew a man so
touchy about an aunt. "Why shouldn't I send a cushion to my aunt?" "Don't get excited," I replied. "I am not objecting; I respect you for
it." He recovered his temper, and went on: "There were four in the window, if you remember, all very much alike, and
each one labelled in plain figures twenty marks. I don't pretend to
speak German fluently, but I can generally make myself understood with a
little effort, and gather the sense of what is said to me, provided they
don't gabble. I went into the shop. A young girl came up to me; she was
a pretty, quiet little soul, one might almost say, demure; not at all the
sort of girl from whom you would have expected such a thing. I was never
more surprised in all my life." "Surprised about what?" I said. [COMPANION_B] always assumes you know the end of the story while he is telling
you the beginning; it is an annoying method. "At what happened," replied [COMPANION_B]; "at what I am telling you. She
smiled and asked me what I wanted. I understood that all right; there
could have been no mistake about that. I put down a twenty mark piece on
the counter and said: "Please give me a cushion." "She stared at me as if I had asked for a feather bed. I thought, maybe,
she had not heard, so I repeated it louder. If I had chucked her under
the chin she could not have looked more surprised or indignant. "She said she thought I must be making a mistake. "I did not want to begin a long conversation and find myself stranded. I
said there was no mistake. I pointed to my twenty mark piece, and
repeated for the third time that I wanted a cushion, 'a twenty mark
cushion.' "Another girl came up, an elder girl; and the first girl repeated to her
what I had just said: she seemed quite excited about it. The second girl
did not believe her--did not think I looked the sort of man who would
want a cushion. To make sure, she put the question to me herself. "'Did you say you wanted a cushion?' she asked. "'I have said it three times,' I answered. 'I will say it again--I want
a cushion.' "She said: 'Then you can't have one.' "I was getting angry by this time. If I hadn't really wanted the thing I
should have walked out of the shop; but there the cushions were in the
window, evidently for sale. I didn't see _why_ I couldn't have one. "I said: 'I will have one!' It is a simple sentence. I said it with
determination. "A third girl came up at this point, the three representing, I fancy, the
whole force of the shop. She was a bright-eyed, saucy-looking little
wench, this last one. On any other occasion I might have been pleased to
see her; now, her coming only irritated me. I didn't see the need of
three girls for this business. "The first two girls started explaining the thing to the third girl, and
before they were half-way through the third girl began to giggle--she was
the sort of girl who would giggle at anything. That done, they fell to
chattering like Jenny Wrens, all three together; and between every halfdozen words they looked across at me; and the more they looked at me the
more the third girl giggled; and before they had finished they were all
three giggling, the little idiots; you might have thought I was a clown,
giving a private performance. "When she was steady enough to move, the third girl came up to me; she
was still giggling. She said: "'If you get it, will you go?' "I did not quite understand her at first, and she repeated it. "'This cushion. When you've got it, will you go--away--at once?' "I was only too anxious to go. I told her so. But, I added I was not
going without it. I had made up my mind to have that cushion now if I
stopped in the shop all night for it. "She rejoined the other two girls. I thought they were going to get me
the cushion and have done with the business. Instead of that, the
strangest thing possible happened. The two other girls got behind the
first girl, all three still giggling, Heaven knows what about, and pushed
her towards me. They pushed her close up to me, and then, before I knew
what was happening, she put her hands on my shoulders, stood up on
tiptoe, and kissed me. After which, burying her face in her apron, she
ran off, followed by the second girl. The third girl opened the door for
me, and so evidently expected me to go, that in my confusion I went,
leaving my twenty marks behind me. I don't say I minded the kiss, though
I did not particularly want it, while I did want the cushion. I don't
like to go back to the shop. I cannot understand the thing at all." I said: "What did you ask for?" He said: "A cushion" I said: "That is what you wanted, I know. What I mean is, what was the
actual German word you said." He replied: "A kuss." I said: "You have nothing to complain of. It is somewhat confusing. A
'kuss' sounds as if it ought to be a cushion, but it is not; it is a
kiss, while a 'kissen' is a cushion. You muddled up the two words--people
have done it before. I don't know much about this sort of thing myself;
but you asked for a twenty mark kiss, and from your description of the
girl some people might consider the price reasonable. Anyhow, I should
not tell [COMPANION_A]. If I remember rightly, he also has an aunt." [COMPANION_B] agreed with me it would be better not.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `ESCALATION` (conf: `0.95`)
- **Temporal Horizon:** `LOCAL` | Secondary: `['MISUNDERSTANDING', 'SOCIAL_EMBARRASSMENT']`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [
    "SOCIAL_EMBARRASSMENT",
    "VERBAL_WIT",
    "ESCALATION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 10,
  "craft_clarity": 8,
  "training_value": 8,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Very rich comic passage containing several complete mechanisms, especially the cushion/kiss misunderstanding and escalating social embarrassment; composite rather than pure."
}
```

---

### Passage 042 [COMPOSITE] — *A Damsel In Distress* (`a_damsel_in_distress_ch25_00388`)

> CHAPTER XXII IN THE LIBRARY Jimmy's first emotion on hearing the footstep was the crude
instinct of self-preservation. All that he was able to think of
at the moment was the fact that he was in a questionable position
and one which would require a good deal of explaining away if he
were found, and his only sensation was a strong desire to avoid
discovery. He made a silent, scrambling leap for the gallery
stairs, and reached their shelter just as the door opened. He
stood there, rigid, waiting to be challenged, but apparently he
had moved in time, for no voice spoke. The door closed so gently
as to be almost inaudible, and then there was silence again. The
room remained in darkness, and it was this perhaps that first
suggested to Jimmy the comforting thought that the intruder was
equally desirous of avoiding the scrutiny of his fellows. He had
taken it for granted in his first panic that he himself was the
only person in that room whose motive for being there would not
have borne inspection. But now, safely hidden in the gallery, out
of sight from the floor below, he had the leisure to consider the
newcomer's movements and to draw conclusions from them. An honest man's first act would surely have been to switch on the
lights. And an honest man would hardly have crept so stealthily.
It became apparent to Jimmy, as he leaned over the rail and tried
to pierce the darkness, that there was sinister work afoot; and
he had hardly reached this conclusion when his mind took a
further leap and he guessed the identity of the soft-footed
person below. It could be none but his old friend Lord Wisbeach,
known to "the boys" as Gentleman Jack. It surprised him that he
had not thought of this before. Then it surprised him that, after
the talk they had only a few hours earlier in that very room,
Gentleman Jack should have dared to risk this raid. At this moment the blackness was relieved as if by the striking
of a match. The man below had brought an electric torch into
play, and now Jimmy could see clearly. He had been right in his
surmise. It was Lord Wisbeach. He was kneeling in front of the
safe. What he was doing to the safe, Jimmy could not see, for the
man's body was in the way; but the electric torch shone on his
face, lighting up grim, serious features quite unlike the amiable
and slightly vacant mask which his lordship was wont to present
to the world. As Jimmy looked, something happened in the pool of
light beyond his vision. Gentleman Jack gave a muttered
exclamation of satisfaction, and then Jimmy saw that the door of
the safe had swung open. The air was full of a penetrating smell
of scorched metal. Jimmy was not an expert in these matters, but
he had read from time to time of modern burglars and their
methods, and he gathered that an oxy-acetylene blow-pipe, with
its flame that cuts steel as a knife cuts cheese, had been at
work. Lord Wisbeach flashed the torch into the open safe, plunged his
hand in, and drew it out again, holding something. Handling this
in a cautious and gingerly manner, he placed it carefully in his
breast pocket. Then he straightened himself. He switched off the
torch, and moved to the window, leaving the rest of his
implements by the open safe. He unfastened the shutter, then
raised the catch of the window. At this point it seemed to Jimmy
that the time had come to interfere. "Tut, tut!" he said in a tone of mild reproof. The effect of the rebuke on Lord Wisbeach was remarkable. He
jumped convulsively away from the window, then, revolving on his
own axis, flashed the torch into every corner of the room. "Who's that?" he gasped. "Conscience!" said Jimmy. Lord Wisbeach had overlooked the gallery in his researches. He
now turned his torch upwards. The light flooded the gallery on
the opposite side of the room from where Jimmy stood. There was a
pistol in Gentleman Jack's hand now. It followed the torch
uncertainly. Jimmy, lying flat on the gallery floor, spoke again. "Throw that gun away, and the torch, too," he said. "I've got you
covered!" The torch flashed above his head, but the raised edge of the
gallery rail protected him. "I'll give you five seconds. If you haven't dropped that gun by
then, I shall shoot!" As he began to count, Jimmy heartily regretted that he had
allowed his appreciation of the dramatic to lead him into this
situation. It would have been so simple to have roused the house
in a prosaic way and avoided this delicate position. Suppose his
bluff did not succeed. Suppose the other still clung to his
pistol at the end of the five seconds. He wished that he had made
it ten instead. Gentleman Jack was an enterprising person, as his
previous acts had showed. He might very well decide to take a
chance. He might even refuse to believe that Jimmy was armed. He
had only Jimmy's word for it. Perhaps he might be as deficient in
simple faith as he had proved to be in Norman blood! Jimmy
lingered lovingly over his count. "Four!" he said reluctantly. There was a breathless moment. Then, to Jimmy's unspeakable
relief, gun and torch dropped simultaneously to the floor. In an
instant Jimmy was himself again. "Go and stand with your face to that wall," he said crisply.
"Hold your hands up!" "Why?" "I'm going to see how many more guns you've got." "I haven't another." "I'd like to make sure of that for myself. Get moving!" Gentleman Jack reluctantly obeyed. When he had reached the wall,
Jimmy came down. He switched on the lights. He felt in the
other's pockets, and almost at once encountered something hard
and metallic. He shook his head reproachfully. "You are very loose and inaccurate in your statements," he said.
"Why all these weapons? I didn't raise my boy to be a soldier!
Now you can turn around and put your hands down." Gentleman Jack's appeared to be a philosophical nature. The
chagrin consequent upon his failure seemed to have left him. He
sat on the arm of a chair and regarded Jimmy without apparent
hostility. He even smiled a faint smile. "I thought I had fixed you, he said. You must have been smarter
than I took you for. I never supposed you would get on to that
drink and pass it up." Understanding of an incident which had perplexed him came to
Jimmy. "Was it you who put that high-ball in my room? Was it doped?" "Didn't you know?" "Well," said Jimmy, "I never knew before that virtue got its
reward so darned quick in this world. I rejected that high-ball
not because I suspected it but out of pure goodness, because I
had made up my mind that I was through with all that sort of
thing." His companion laughed. If Jimmy had had a more intimate
acquaintance with the resourceful individual whom the "boys"
called Gentleman Jack, he would have been disquieted by that
laugh. It was an axiom among those who knew him well, that when
Gentleman Jack chuckled in the reflective way, he generally had
something unpleasant up his sleeve. "It's your lucky night," said Gentleman Jack. "It looks like it." "Well, it isn't over yet." "Very nearly. You had better go and put that test-tube back in
what is left of the safe now. Did you think I had forgotten it?" "What test-tube?" "Come, come, old friend! The one filled with Partridge's
explosive, which you have in your breast-pocket." Gentleman Jack laughed again. Then he moved towards the safe. "Place it gently on the top shelf," said Jimmy. The next moment every nerve in his body was leaping and
quivering. A great shout split the air. Gentleman Jack,
apparently insane, was giving tongue at the top of his voice. "Help! Help! Help!" The conversation having been conducted up to this point in
undertones, the effect of this unexpected uproar was like an
explosion. The cries seemed to echo round the room and shake the
very walls. For a moment Jimmy stood paralysed, staring feebly;
then there was a sudden deafening increase in the din. Something
living seemed to writhe and jump in his hand. He dropped it
incontinently, and found himself gazing in a stupefied way at a
round, smoking hole in the carpet. Such had been the effect of
Gentleman Jack's unforeseen outburst that he had quite forgotten
that he held the revolver, and he had been unfortunate enough at
this juncture to pull the trigger. There was a sudden rush and a swirl of action. Something hit
Jimmy under the chin. He staggered back, and when he had
recovered himself found himself looking into the muzzle of the
revolver which had nearly blown a hole in his foot a moment back.
The sardonic face of Gentleman Jack smiled grimly over the
barrel. "I told you the night wasn't over yet!" he said. The blow under the chin had temporarily dulled Jimmy's mentality.
He stood, swallowing and endeavouring to pull himself together
and to get rid of a feeling that his head was about to come off.
He backed to the desk and steadied himself against it. As he did so, a voice from behind him spoke. "Whassall this?" He turned his head. A curious procession was filing in through
the open French window. First came Mr. Crocker, still wearing his
hideous mask; then a heavily bearded individual with round
spectacles, who looked like an automobile coming through a
haystack; then Ogden Ford, and finally a sturdy,
determined-looking woman with glittering but poorly co-ordinated
eyes, who held a large revolver in her unshaking right hand and
looked the very embodiment of the modern female who will stand no
nonsense. It was part of the nightmare-like atmosphere which
seemed to brood inexorably over this particular night that this
person looked to Jimmy exactly like the parlour-maid who had come
to him in this room in answer to the bell and who had sent his
father to him. Yet how could it be she? Jimmy knew little of the
habits of parlour-maids, but surely they did not wander about
with revolvers in the small hours? While he endeavoured feverishly to find reason in this chaos, the
door opened and a motley crowd, roused from sleep by the cries,
poured in. Jimmy, turning his head back again to attend to this
invasion, perceived Mrs. Pett, Ann, two or three of the geniuses,
and Willie Partridge, in various stages of _negligee_ and babbling
questions. The woman with the pistol, assuming instant and unquestioned
domination of the assembly, snapped out an order. "Shutatdoor!" Somebody shut the door. "Now, whassall this?" she said, turning to Gentleman Jack.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.25`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "PHYSICAL_COMPLICATION",
  "secondary_mechanisms": [
    "ESCALATION",
    "MISUNDERSTANDING",
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 10,
  "craft_clarity": 10,
  "training_value": 10,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Strong farce: burglary, bluffing, multiple weapons, accidental gunfire, and a chaotic arrival create escalating physical complications with deadpan verbal turns."
}
```

---

### Passage 043 [COMPOSITE] — *My Man Jeeves* (`my_man_jeeves_ch17_00287`)

> "and put up the shutters. The next two nights I didn't come across them, but the night after that I was sitting by myself at the Maison Pierre when somebody tapped me on the shoulder-blade, and I found Rocky standing beside me, with a sort of mixed expression of wistfulness and apoplexy on his face. How the chappie had contrived to wear my evening clothes so many times without disaster was a mystery to me. He confided later that early in the proceedings he had slit the waistcoat up the back and that that had helped a bit. For a moment I had the idea that he had managed to get away from his aunt for the evening; but, looking past him, I saw that she was in again. She was at a table over by the wall, looking at me as if I were something the management ought to be complained to about," I had only read a couple of his letters, but they certainly gave the impression that poor old Rocky was by way of being the hub of New York night life, and that, if by any chance he failed to show up at a cabaret, the management said: "What's the use? [PROTAGONIST], old scout," said Rocky, in a quiet, sort of crushed voice, "we've always been pals, haven't we? I mean, you know I'd do you a good turn if you asked me?" "My dear old lad," I said.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `ESCALATION` (conf: `0.25`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "SOCIAL_EMBARRASSMENT",
  "secondary_mechanisms": [
    "ESCALATION",
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Rocky's ill-fitting use of the narrator's clothes and his aunt's disapproving stare create a socially awkward situation that is then extended through restrained narration."
}
```

---

### Passage 044 [COMPOSITE] — *Right Ho* (`right_ho_ch18_07025`)

> and I was back in the old flat, lying in the old arm-chair, with my feet upon the good old table. I had just come from seeing dear old Rocky off to his country cottage, and an hour before he had seen his aunt off to whatever hamlet it was that she was the curse of; so we were alone at last. "[COMPANION], there's no place like home - what?" "Very true, sir." "The jolly old roof-tree, and all that sort of thing - what?" "Precisely, sir." I lit another cigarette. "[COMPANION]." "Sir?" "Do you know, at one point in the business I really thought you were baffled." "Indeed, sir?" "When did you get the idea of taking Miss [FRIEND] to the meeting? It was pure genius!" "Thank you, sir. It came to me a little suddenly, one morning when I was thinking of my aunt, sir." "Your aunt? The hansom cab one?" "Yes, sir. I recollected that, whenever we observed one of her attacks coming on, we used to send for the clergyman of the parish. We always found that if he talked to her a while of higher things it diverted her mind from hansom cabs. It occurred to me that the same treatment might prove efficacious in the case of Miss [FRIEND]." I was stunned by the man's resource. "It's brain," I said; "pure brain! What do you do to get like that, [COMPANION]? I believe you must eat a lot of fish, or something. Do you eat a lot of fish, [COMPANION]?" "No, sir." "Oh, well, then, it's just a gift, I take it; and if you aren't born that way there's no use worrying." "Precisely, sir," said [COMPANION]. "If I might make the suggestion, sir, I should not continue to wear your present tie. The green shade gives you a slightly bilious air. I should strongly advocate the blue with the red domino pattern instead, sir." "All right, [COMPANION]." I said humbly. "You know!" THE END

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "UNREVIEWED",
  "craft_stratum": "UNREVIEWED",
  "primary_mechanism": null,
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": null,
  "escalation_accurate": null,
  "reversal_accurate": null,
  "payoff_accurate": null,
  "literary_quality": null,
  "craft_clarity": null,
  "training_value": null,
  "keep_verdict": "UNREVIEWED",
  "detector_correct": null,
  "notes": ""
}
```

---

### Passage 045 [COMPOSITE] — *Something Fresh* (`something_fresh_ch5_06801`)

> "How are you feeling after the journey, Mr. Marson?," said a voice
from the other side of the table; and Ashe, looking up
gratefully, found Joan's eyes looking into his with a curiously
amused expression.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `ESCALATION` (conf: `0.25`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "UNREVIEWED",
  "craft_stratum": "UNREVIEWED",
  "primary_mechanism": null,
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": null,
  "escalation_accurate": null,
  "reversal_accurate": null,
  "payoff_accurate": null,
  "literary_quality": null,
  "craft_clarity": null,
  "training_value": null,
  "keep_verdict": "UNREVIEWED",
  "detector_correct": null,
  "notes": ""
}
```

---

### Passage 046 [COMPOSITE] — *The Inimitable Jeeves* (`the_inimitable_jeeves_ch23_07867`)

> "and the city's common seal was set to the so-called," The mayor, aldermen, and citizens, after a hasty consultation, gave their
assent, but with the reservation "saving unto them all their liberties and
customs, charter"
which the deputation had brought.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "UNREVIEWED",
  "craft_stratum": "UNREVIEWED",
  "primary_mechanism": null,
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": null,
  "escalation_accurate": null,
  "reversal_accurate": null,
  "payoff_accurate": null,
  "literary_quality": null,
  "craft_clarity": null,
  "training_value": null,
  "keep_verdict": "UNREVIEWED",
  "detector_correct": null,
  "notes": ""
}
```

---

### Passage 047 [COMPOSITE] — *The Little Nugget* (`the_little_nugget_ch1_07185`)

> "pay for thim an' take thim, or don't pay for thim and leave thim be. Rules is rules, Misther Morehouse, an' Mike Flannery's not goin' to be called down fer breakin' of thim," "Do as you loike, then!" shouted Flannery, "But, you everlastingly stupid idiot!" shouted Mr.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "UNREVIEWED",
  "craft_stratum": "UNREVIEWED",
  "primary_mechanism": null,
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": null,
  "escalation_accurate": null,
  "reversal_accurate": null,
  "payoff_accurate": null,
  "literary_quality": null,
  "craft_clarity": null,
  "training_value": null,
  "keep_verdict": "UNREVIEWED",
  "detector_correct": null,
  "notes": ""
}
```

---

### Passage 048 [COMPOSITE] — *The Man Upstairs* (`the_man_upstairs_ch6_02510`)

> "asked Caroline, almost fiercely," "Why don't you put the lamp on this table, as she says? Why do you act so, Rebecca?" "I should think you WOULD ask her that," said Mrs.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "UNREVIEWED",
  "craft_stratum": "UNREVIEWED",
  "primary_mechanism": null,
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": null,
  "escalation_accurate": null,
  "reversal_accurate": null,
  "payoff_accurate": null,
  "literary_quality": null,
  "craft_clarity": null,
  "training_value": null,
  "keep_verdict": "UNREVIEWED",
  "detector_correct": null,
  "notes": ""
}
```

---

### Passage 049 [COMPOSITE] — *Their Mutual Child* (`their_mutual_child_ch28_04968`)

> "Advancement of Science," Yet Langley said nothing new, and taught nothing that one
might not have learned from Lord Bacon, three hundred years before; but
though one should have known the as well as
one knew the "Comedy of Errors," the literary knowledge counted for
nothing until some teacher should show how to apply it.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "UNREVIEWED",
  "craft_stratum": "UNREVIEWED",
  "primary_mechanism": null,
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": null,
  "escalation_accurate": null,
  "reversal_accurate": null,
  "payoff_accurate": null,
  "literary_quality": null,
  "craft_clarity": null,
  "training_value": null,
  "keep_verdict": "UNREVIEWED",
  "detector_correct": null,
  "notes": ""
}
```

---

### Passage 050 [COMPOSITE] — *Three Men In A Boat* (`three_men_in_a_boat_ch10_08599`)

> CHAPTER X. Our first night. - Under canvas. - An appeal for help. - Contrariness of
tea-kettles, how to overcome. - Supper. - How to feel virtuous. - Wanted! a
comfortably-appointed, well-drained desert island, neighbourhood of
South Pacific Ocean preferred. - Funny thing that happened to [COMPANION_B]'s
father. - a restless night. [COMPANION_A] and I began to think that Bell Weir lock must have been done
away with after the same manner. [COMPANION_B] had towed us up to Staines, and
we had taken the boat from there, and it seemed that we were dragging
fifty tons after us, and were walking forty miles. It was half-past
seven when we were through, and we all got in, and sculled up close to
the left bank, looking out for a spot to haul up in. We had originally intended to go on to Magna Charta Island, a sweetly
pretty part of the river, where it winds through a soft, green valley,
and to camp in one of the many picturesque inlets to be found round
that tiny shore. But, somehow, we did not feel that we yearned for the
picturesque nearly so much now as we had earlier in the day. A bit of
water between a coal-barge and a gas-works would have quite satisfied
us for that night. We did not want scenery. We wanted to have our
supper and go to bed. However, we did pull up to the point - "Picnic
Point," it is called - and dropped into a very pleasant nook under a
great elm-tree, to the spreading roots of which we fastened the boat. Then we thought we were going to have supper (we had dispensed with
tea, so as to save time), but [COMPANION_B] said no; that we had better get
the canvas up first, before it got quite dark, and while we could see
what we were doing. Then, he said, all our work would be done, and we
could sit down to eat with an easy mind. That canvas wanted more putting up than I think any of us had bargained
for. It looked so simple in the abstract. You took five iron arches,
like gigantic croquet hoops, and fitted them up over the boat, and then
stretched the canvas over them, and fastened it down: it would take
quite ten minutes, we thought. That was an under-estimate. We took up the hoops, and began to drop them into the sockets placed
for them. You would not imagine this to be dangerous work; but, looking
back now, the wonder to me is that any of us are alive to tell the
tale. They were not hoops, they were demons. First they would not fit
into their sockets at all, and we had to jump on them, and kick them,
and hammer at them with the boat-hook; and, when they were in, it
turned out that they were the wrong hoops for those particular sockets,
and they had to come out again. But they would not come out, until two of us had gone and struggled
with them for five minutes, when they would jump up suddenly, and
try and throw us into the water and drown us. They had hinges in the
middle, and, when we were not looking, they nipped us with these hinges
in delicate parts of the body; and, while we were wrestling with one
side of the hoop, and endeavouring to persuade it to do its duty, the
other side would come behind us in a cowardly manner, and hit us over
the head. We got them fixed at last, and then all that was to be done was to
arrange the covering over them. [COMPANION_B] unrolled it, and fastened one
end over the nose of the boat. [COMPANION_A] stood in the middle to take it
from [COMPANION_B] and roll it on to me, and I kept by the stern to receive
it. It was a long time coming down to me. [COMPANION_B] did his part all
right, but it was new work to [COMPANION_A], and he bungled it. How he managed it I do not know, he could not explain himself; but
by some mysterious process or other he succeeded, after ten minutes
of superhuman effort, in getting himself completely rolled up in
it. He was so firmly wrapped round and tucked in and folded over,
that he could not get out. He, of course, made frantic struggles for
freedom - the birthright of every Englishman, - and, in doing so (I learned
this afterwards), knocked over [COMPANION_B]; and then [COMPANION_B], swearing at
[COMPANION_A], began to struggle too, and got _himself_ entangled and rolled
up. [Picture: Watching and waiting] I knew nothing about all this at the
time. I did not understand the business at all myself. I had been
told to stand where I was, and wait till the canvas came to me, and
[DOG_COMPANION] and I stood there and waited, both as good as gold. We
could see the canvas being violently jerked and tossed about, pretty
considerably; but we supposed this was part of the method, and did not
interfere. We also heard much smothered language coming from underneath it, and
we guessed that they were finding the job rather troublesome, and
concluded that we would wait until things had got a little simpler
before we joined in. We waited some time, but matters seemed to get only more and more
involved, until, at last, [COMPANION_B]'s head came wriggling out over the
side of the boat, and spoke up. It said: "Give us a hand here, can't you, you cuckoo; standing there like a
stuffed mummy, when you see we are both being suffocated, you dummy!" I never could withstand an appeal for help, so I went and undid them;
not before it was time, either, for [COMPANION_A] was nearly black in the face. It took us half an hour's hard labour, after that, before it was
properly up, and then we cleared the decks, and got out supper. We put
the kettle on to boil, up in the nose of the boat, and went down to the
stern and pretended to take no notice of it, but set to work to get the
other things out. That is the only way to get a kettle to boil up the river. If it sees
that you are waiting for it and are anxious, it will never even sing.
You have to go away and begin your meal, as if you were not going to
have any tea at all. You must not even look round at it. Then you will
soon hear it sputtering away, mad to be made into tea. It is a good plan, too, if you are in a great hurry, to talk very
loudly to each other about how you don't need any tea, and are not
going to have any. You get near the kettle, so that it can overhear
you, and then you shout out, "I don't want any tea; do you, [COMPANION_B]?"
to which [COMPANION_B] shouts back, "Oh, no, I don't like tea; we'll have
lemonade instead - tea's so indigestible." Upon which the kettle boils
over, and puts the stove out. We adopted this harmless bit of trickery, and the result was that, by
the time everything else was ready, the tea was waiting. Then we lit
the lantern, and squatted down to supper. We wanted that supper. For five-and-thirty minutes not a sound was heard throughout the
length and breadth of that boat, save the clank of cutlery and
crockery, and the steady grinding of four sets of molars. At the end of
five-and-thirty minutes, [COMPANION_A] said, "Ah!" and took his left leg out
from under him and put his right one there instead. Five minutes afterwards, [COMPANION_B] said, "Ah!" too, and threw his plate
out on the bank; and, three minutes later than that, [DOG_COMPANION] gave
the first sign of contentment he had exhibited since we had started,
and rolled over on his side, and spread his legs out; and then I said,
"Ah!" and bent my head back, and bumped it against one of the hoops,
but I did not mind it. I did not even swear. How good one feels when one is full - how satisfied with ourselves
and with the world! People who have tried it, tell me that a clear
conscience makes you very happy and contented; but a full stomach
does the business quite as well, and is cheaper, and more easily
obtained. One feels so forgiving and generous after a substantial and
well-digested meal - so noble-minded, so kindly-hearted. It is very strange, this domination of our intellect by our digestive
organs. We cannot work, we cannot think, unless our stomach wills so.
It dictates to us our emotions, our passions. After eggs and bacon,
it says, "Work!" After beefsteak and porter, it says, "Sleep!" After
a cup of tea (two spoonsful for each cup, and don't let it stand
more than three minutes), it says to the brain, "Now, rise, and show
your strength. Be eloquent, and deep, and tender; see, with a clear
eye, into Nature and into life; spread your white wings of quivering
thought, and soar, a god-like spirit, over the whirling world beneath
you, up through long lanes of flaming stars to the gates of eternity!" After hot muffins, it says, "Be dull and soulless, like a beast of the
field - a brainless animal, with listless eye, unlit by any ray of fancy,
or of hope, or fear, or love, or life." And after brandy, taken in
sufficient quantity, it says, "Now, come, fool, grin and tumble, that
your fellow-men may laugh - drivel in folly, and splutter in senseless
sounds, and show what a helpless ninny is poor man whose wit and will
are drowned, like kittens, side by side, in half an inch of alcohol." We are but the veriest, sorriest slaves of our stomach. Reach not after
morality and righteousness, my friends; watch vigilantly your stomach,
and diet it with care and judgment. Then virtue and contentment will
come and reign within your heart, unsought by any effort of your own;
and you will be a good citizen, a loving husband, and a tender father - a
noble, pious man. Before our supper, [COMPANION_A] and [COMPANION_B] and I were quarrelsome and
snappy and ill-tempered; after our supper, we sat and beamed on one
another, and we beamed upon the dog, too. We loved each other, we loved
everybody. [COMPANION_A], in moving about, trod on [COMPANION_B]'s corn. Had this
happened before supper, [COMPANION_B] would have expressed wishes and desires
concerning [COMPANION_A]'s fate in this world and the next that would have
made a thoughtful man shudder. As it was, he said: "Steady, old man; 'ware wheat." And [COMPANION_A], instead of merely observing, in his most unpleasant tones,
that a fellow could hardly help treading on some bit of [COMPANION_B]'s foot,
if he had to move about at all within ten yards of where [COMPANION_B] was
sitting, suggesting that [COMPANION_B] never ought to come into an ordinary
sized boat with feet that length, and advising him to hang them over
the side, as he would have done before supper, now said: "Oh, I'm so
sorry, old chap; I hope I haven't hurt you." [Picture: Smoking pipes] And [COMPANION_B] said: "Not at all;" that it was his
fault; and [COMPANION_A] said no, it was his. It was quite pretty to hear them. We lit our pipes, and sat, looking out on the quiet night, and talked. [COMPANION_B] said why could not we be always like this - away from the world,
with its sin and temptation, leading sober, peaceful lives, and doing
good. I said it was the sort of thing I had often longed for myself;
and we discussed the possibility of our going away, we four, to some
handy, well-fitted desert island, and living there in the woods. [COMPANION_A] said that the danger about desert islands, as far as he had
heard, was that they were so damp: but [COMPANION_B] said no, not if properly
drained. And then we got on to drains, and that put [COMPANION_B] in mind of a very
funny thing that happened to his father once. He said his father was
travelling with another fellow through Wales, and, one night, they
stopped at a little inn, where there were some other fellows, and they
joined the other fellows, and spent the evening with them. They had a very jolly evening, and sat up late, and, by the time they
came to go to bed, they (this was when [COMPANION_B]'s father was a very young
man) were slightly jolly, too. They ([COMPANION_B]'s father and [COMPANION_B]'s
father's friend) were to sleep in the same room, but in different beds.
They took the candle, and went up. The candle lurched up against the
wall when they got into the room, and went out, and they had to undress
and grope into bed in the dark. This they did; but, instead of getting
into separate beds, as they thought they were doing, they both climbed
into the same one without knowing it - one getting in with his head
at the top, and the other crawling in from the opposite side of the
compass, and lying with his feet on the pillow. There was silence for a moment, and then [COMPANION_B]'s father said: "Joe!" "What's the matter, Tom?" replied Joe's voice from the other end of the
bed. "Why, there's a man in my bed," said [COMPANION_B]'s father; "here's his feet
on my pillow." "Well, it's an extraordinary thing, Tom," answered the other; "but I'm
blest if there isn't a man in my bed, too!" "What are you going to do?" asked [COMPANION_B]'s father. "Well, I'm going to chuck him out," replied Joe. "So am I," said [COMPANION_B]'s father, valiantly. There was a brief struggle, followed by two heavy bumps on the floor,
and then a rather doleful voice said: "I say, Tom!" "Yes!" "How have you got on?" "Well, to tell you the truth, my man's chucked _me_ out." "So's mine! I say, I don't think much of this inn, do you?" "What was the name of that inn?" said [COMPANION_A]. "The Pig and Whistle," said [COMPANION_B]. "Why?" "Ah, no, then it isn't the same," replied [COMPANION_A]. "What do you mean?" queried [COMPANION_B]. "Why it's so curious," murmured [COMPANION_A], "but precisely that very same
thing happened to _my_ father once at a country inn. I've often heard
him tell the tale. I thought it might have been the same inn." We turned in at ten that night, and I thought I should sleep well,
being tired; but I didn't. As a rule, I undress and put my head on the
pillow, and then somebody bangs at the door, and says it is half-past
eight: but, to-night, everything seemed against me; the novelty of
it all, the hardness of the boat, the cramped position (I was lying
with my feet under one seat, and my head on another), the sound of the
lapping water round the boat, and the wind among the branches, kept me
restless and disturbed. I did get to sleep for a few hours, and then some part of the boat
which seemed to have grown up in the night - for it certainly was not
there when we started, and it had disappeared by the morning - kept
digging into my spine. I slept through it for a while, dreaming that I
had swallowed a sovereign, and that they were cutting a hole in my back
with a gimlet, so as to try and get it out. I thought it very unkind
of them, and I told them I would owe them the money, and they should
have it at the end of the month. But they would not hear of that, and
said it would be much better if they had it then, because otherwise the
interest would accumulate so. I got quite cross with them after a bit,
and told them what I thought of them, and then they gave the gimlet
such an excruciating wrench that I woke up. The boat seemed stuffy, and my head ached; so I thought I would step
out into the cool night-air. I slipped on what clothes I could find
about - some of my own, and some of [COMPANION_B]'s and [COMPANION_A]'s - and crept under
the canvas on to the bank. It was a glorious night. The moon had sunk, and left the quiet earth
alone with the stars. It seemed as if, in the silence and the hush,
while we her children slept, they were talking with her, their
sister - conversing of mighty mysteries in voices too vast and deep for
childish human ears to catch the sound. They awe us, these strange stars, so cold, so clear. We are as children
whose small feet have strayed into some dim-lit temple of the god they
have been taught to worship but know not; and, standing where the
echoing dome spans the long vista of the shadowy light, glance up, half
hoping, half afraid to see some awful vision hovering there. And yet it seems so full of comfort and of strength, the night. In its
great presence, our small sorrows creep away, ashamed. The day has been
so full of fret and care, and our hearts have been so full of evil and
of bitter thoughts, and the world has seemed so hard and wrong to us.
Then Night, like some great loving mother, gently lays her hand upon
our fevered head, and turns our little tear-stained faces up to hers,
and smiles; and, though she does not speak, we know what she would say,
and lay our hot flushed cheek against her bosom, and the pain is gone. Sometimes, our pain is very deep and real, and we stand before her very
silent, because there is no language for our pain, only a moan. Night's
heart is full of pity for us: she cannot ease our aching; she takes our
hand in hers, and the little world grows very small and very far away
beneath us, and, borne on her dark wings, we pass for a moment into a
mightier Presence than her own, and in the wondrous light of that great
Presence, all human life lies like a book before us, and we know that
Pain and Sorrow are but the angels of God. Only those who have worn the crown of suffering can look upon that
wondrous light; and they, when they return, may not speak of it, or
tell the mystery they know. Once upon a time, through a strange country, there rode some goodly
knights, and their path lay by a deep wood, where tangled briars grew
very thick and strong, and tore the flesh of them that lost their way
therein. And the leaves of the trees that grew in the wood were very
dark and thick, so that no ray of light came through the branches to
lighten the gloom and sadness. And, as they passed by that dark wood, one knight of those that rode,
missing his comrades, wandered far away, and returned to them no more;
and they, sorely grieving, rode on without him, mourning him as one
dead. Now, when they reached the fair castle towards which they had been
journeying, they stayed there many days, and made merry; and one night,
as they sat in cheerful ease around the logs that burned in the great
hall, and drank a loving measure, there came the comrade they had lost,
and greeted them. His clothes were ragged, like a beggar's, and many
sad wounds were on his sweet flesh, but upon his face there shone a
great radiance of deep joy. And they questioned him, asking him what had befallen him: and he told
them how in the dark wood he had lost his way, and had wandered many
days and nights, till, torn and bleeding, he had lain him down to die. Then, when he was nigh unto death, lo! through the savage gloom there
came to him a stately maiden, and took him by the hand and led him on
through devious paths, unknown to any man, until upon the darkness of
the wood there dawned a light such as the light of day was unto but as
a little lamp unto the sun; and, in that wondrous light, our way-worn
knight saw as in a dream a vision, and so glorious, so fair the vision
seemed, that of his bleeding wounds he thought no more, but stood as
one entranced, whose joy is deep as is the sea, whereof no man can tell
the depth. And the vision faded, and the knight, kneeling upon the ground, thanked
the good saint who into that sad wood had strayed his steps, so he had
seen the vision that lay there hid. And the name of the dark forest was Sorrow; but of the vision that the
good knight saw therein we may not speak nor tell.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.25`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "UNREVIEWED",
  "craft_stratum": "UNREVIEWED",
  "primary_mechanism": null,
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": null,
  "escalation_accurate": null,
  "reversal_accurate": null,
  "payoff_accurate": null,
  "literary_quality": null,
  "craft_clarity": null,
  "training_value": null,
  "keep_verdict": "UNREVIEWED",
  "detector_correct": null,
  "notes": ""
}
```

---

### Passage 051 [COMPOSITE] — *Three Men On The Bummel* (`three_men_on_the_bummel_chNone_00099`)

> And at that the bad sheep laughed--laughed distinctly and undoubtedly, a husky, vulgar laugh; and, while her friend stood glued to the ground, too astonished to move, she changed her note for the first time and bleated:  "Go-o-o-d, ve-e-ry go-o-o-d! Be-e-e-est sho-o-o-ot he-e-e's ma-a-a-de!"  I would have given half-a-crown if it had been she I had hit instead of the other one

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "UNREVIEWED",
  "craft_stratum": "UNREVIEWED",
  "primary_mechanism": null,
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": null,
  "escalation_accurate": null,
  "reversal_accurate": null,
  "payoff_accurate": null,
  "literary_quality": null,
  "craft_clarity": null,
  "training_value": null,
  "keep_verdict": "UNREVIEWED",
  "detector_correct": null,
  "notes": ""
}
```

---

### Passage 052 [COMPOSITE] — *A Damsel In Distress* (`a_damsel_in_distress_ch29_07583`)

> "Uncle Peter," The words "Uncle" and "Aunt", where used with a name
( "Aunt Nesta"), were capitalized in the original
serialized and UK editions, but lower-cased in the US edition, so I have
retained the lower-case.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "UNREVIEWED",
  "craft_stratum": "UNREVIEWED",
  "primary_mechanism": null,
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": null,
  "escalation_accurate": null,
  "reversal_accurate": null,
  "payoff_accurate": null,
  "literary_quality": null,
  "craft_clarity": null,
  "training_value": null,
  "keep_verdict": "UNREVIEWED",
  "detector_correct": null,
  "notes": ""
}
```

---

### Passage 053 [COMPOSITE] — *My Man Jeeves* (`my_man_jeeves_ch17_02757`)

> "that roused dear old Rocky like a trumpet call. It must have brought home to him the realisation that a miracle had come off and saved him from being cut out of Aunt Isabel's. At any rate, as she said it he perked up, let go of the table, and faced her with gleaming eyes," Won't you, for my sake, try, [FRIEND]? Won't you go back to the country to-morrow and begin the struggle? Little by little, if you use your will - - " I can't help thinking it must have been that word "will Do you want me to go back to the country, Aunt Isabel?" "Yes.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `ESCALATION` (conf: `0.25`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "UNREVIEWED",
  "craft_stratum": "UNREVIEWED",
  "primary_mechanism": null,
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": null,
  "escalation_accurate": null,
  "reversal_accurate": null,
  "payoff_accurate": null,
  "literary_quality": null,
  "craft_clarity": null,
  "training_value": null,
  "keep_verdict": "UNREVIEWED",
  "detector_correct": null,
  "notes": ""
}
```

---

### Passage 054 [COMPOSITE] — *Right Ho* (`right_ho_ch18_00925`)

> "Yes, sir. I recollected that, whenever we observed one of her attacks coming on, we used to send for the clergyman of the parish. We always found that if he talked to her a while of higher things it diverted her mind from hansom cabs. It occurred to me that the same treatment might prove efficacious in the case of Miss [FRIEND]," " "Your aunt? The hansom cab one?" I was stunned by the man's resource.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "UNREVIEWED",
  "craft_stratum": "UNREVIEWED",
  "primary_mechanism": null,
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": null,
  "escalation_accurate": null,
  "reversal_accurate": null,
  "payoff_accurate": null,
  "literary_quality": null,
  "craft_clarity": null,
  "training_value": null,
  "keep_verdict": "UNREVIEWED",
  "detector_correct": null,
  "notes": ""
}
```

---

### Passage 055 [COMPOSITE] — *Something Fresh* (`something_fresh_ch9_02212`)

> Speaker: Character | Target Emotion: Fearful
"Now, my dear Baxter," said the earl impatiently, "please tell me
once again why you have brought me in here.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "UNREVIEWED",
  "craft_stratum": "UNREVIEWED",
  "primary_mechanism": null,
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": null,
  "escalation_accurate": null,
  "reversal_accurate": null,
  "payoff_accurate": null,
  "literary_quality": null,
  "craft_clarity": null,
  "training_value": null,
  "keep_verdict": "UNREVIEWED",
  "detector_correct": null,
  "notes": ""
}
```

---

### Passage 056 [COMPOSITE] — *The Inimitable Jeeves* (`the_inimitable_jeeves_ch21_01257`)

> "from necessity," London submitted, the citizens accepting the rule of the Norman Conqueror
as they had formerly accepted that of Cnut the Dane, An
embassy was despatched to Berkhampstead, comprising the Archbishop of
York, the young Atheling, the earls Edwine and Morkere, and "all the best
men of London," to render homage and give hostages,(80) and thus it was,
that within three months of his landing, William was acknowledged as the
lawfully elected King of England, and, as such, he crowned himself at
Westminster, promising to govern the nation as well as any king before him
if they would be faithful to him.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "UNREVIEWED",
  "craft_stratum": "UNREVIEWED",
  "primary_mechanism": null,
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": null,
  "escalation_accurate": null,
  "reversal_accurate": null,
  "payoff_accurate": null,
  "literary_quality": null,
  "craft_clarity": null,
  "training_value": null,
  "keep_verdict": "UNREVIEWED",
  "detector_correct": null,
  "notes": ""
}
```

---

### Passage 057 [COMPOSITE] — *The Little Nugget* (`the_little_nugget_ch1_04253`)

> "Morgan, head of the Tariff Department, when he received this letter, laughed. He read it again and became serious," I paid out so far two dollars for cabbage which they like shall I put in bill for same what? By [COMPANION_B]!" he said, "Flannery is right, 'pigs is pigs.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "UNREVIEWED",
  "craft_stratum": "UNREVIEWED",
  "primary_mechanism": null,
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": null,
  "escalation_accurate": null,
  "reversal_accurate": null,
  "payoff_accurate": null,
  "literary_quality": null,
  "craft_clarity": null,
  "training_value": null,
  "keep_verdict": "UNREVIEWED",
  "detector_correct": null,
  "notes": ""
}
```

---

### Passage 058 [COMPOSITE] — *The Man Upstairs* (`the_man_upstairs_ch32_01625`)

> "is spoken like my brother. But what are the proofs?," "That," said I, He replied, "Pleyel informed me that, in going to your house, his attention was attracted by two voices.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "UNREVIEWED",
  "craft_stratum": "UNREVIEWED",
  "primary_mechanism": null,
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": null,
  "escalation_accurate": null,
  "reversal_accurate": null,
  "payoff_accurate": null,
  "literary_quality": null,
  "craft_clarity": null,
  "training_value": null,
  "keep_verdict": "UNREVIEWED",
  "detector_correct": null,
  "notes": ""
}
```

---

### Passage 059 [COMPOSITE] — *Their Mutual Child* (`their_mutual_child_ch16_07386`)

> "Yes!," said
Mr Reed; "I noticed this at the sale; but it's not Rafael!" Adams,
feeling himself incompetent to discuss this subject, reported the
result to Palgrave, who said that Reed knew nothing about it.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "UNREVIEWED",
  "craft_stratum": "UNREVIEWED",
  "primary_mechanism": null,
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": null,
  "escalation_accurate": null,
  "reversal_accurate": null,
  "payoff_accurate": null,
  "literary_quality": null,
  "craft_clarity": null,
  "training_value": null,
  "keep_verdict": "UNREVIEWED",
  "detector_correct": null,
  "notes": ""
}
```

---

### Passage 060 [COMPOSITE] — *Three Men In A Boat* (`three_men_in_a_boat_ch17_02474`)

> "Ah! you may well say that, sir," replied the man; and then, after a
pull at his beer, he added, "Maybe you wasn't here, sir, when that fish
was caught?".

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "UNREVIEWED",
  "craft_stratum": "UNREVIEWED",
  "primary_mechanism": null,
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": null,
  "escalation_accurate": null,
  "reversal_accurate": null,
  "payoff_accurate": null,
  "literary_quality": null,
  "craft_clarity": null,
  "training_value": null,
  "keep_verdict": "UNREVIEWED",
  "detector_correct": null,
  "notes": ""
}
```

---

### Passage 061 [COMPOSITE] — *Three Men On The Bummel* (`three_men_on_the_bummel_ch12_02031`)

> Speaker: Character | Target Emotion: Calm / Conversational
"Tell me," I said--I was curious on the subject--"what language was it
you spoke when you first came in?".

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 8,
  "craft_clarity": 8,
  "training_value": 8,
  "keep_verdict": "KEEP",
  "detector_correct": true,
  "notes": "Clear comic misunderstanding with a literal interpretation driving the scene."
}
```

---

### Passage 062 [COMPOSITE] — *A Damsel In Distress* (`a_damsel_in_distress_ch19_04545`)

> "You have been so kind to me, Mrs. Pett," said Lord Wisbeach with
feeling, "that it is surely only right that I should try to make
some return.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [
    "VERBAL_WIT",
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Comic problem grows through repeated attempts to manage an absurd situation."
}
```

---

### Passage 063 [COMPOSITE] — *My Man Jeeves* (`my_man_jeeves_ch1_05572`)

> "It is the way these New York apartments are constructed, sir. Quite unlike our London houses. The partitions between the rooms are of the flimsiest nature. With no wish to overhear, I have sometimes heard Mr. Corcoran expressing himself with a generous strength on the subject I have mentioned," " "How on earth did you know that he was fond of birds?" "Oh! Well?" "Why should not the young lady write a small volume, to be entitled - let us say - _The Children's Book of American Birds_, and dedicate it to Mr.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 1,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Editorial/expository material without a self-contained comic engine."
}
```

---

### Passage 064 [COMPOSITE] — *Right Ho* (`right_ho_ch5_02334`)

> Speaker: Why | Target Emotion: Fearful
"If the Duke of Chiswick is his uncle," I said, "why hasn't he a title? Why isn't he Lord What-Not?" "Mr.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "DEADPAN_REACTION",
  "secondary_mechanisms": [
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "High-stakes situation is answered with conspicuously calm, matter-of-fact reaction."
}
```

---

### Passage 065 [COMPOSITE] — *Something Fresh* (`something_fresh_ch12_08476`)

> CHAPTER XII The Earl of Emsworth sat by the sick bed and regarded the
Honorable Freddie almost tenderly. "I fear, Freddie, my dear boy, this has been a great shock to
you." "Eh? What? Yes--rather! Deuce of a shock, gov'nor." "I have been thinking it over, my boy, and perhaps I have been a
little hard on you. When your ankle is better I have decided to
renew your allowance; and you may return to London, as you do not
seem happy in the country. Though how any reasonable being can
prefer--" The Honorable Freddie started, pop-eyed, to a sitting posture. "My word! Not really?" His father nodded. "I say, gov'nor, you really are a topper! You really are, you
know! I know just how you feel about the country and the jolly
old birds and trees and chasing the bally slugs off the young
geraniums and all that sort of thing, but somehow it's never
quite hit me the same way. It's the way I'm built, I suppose. I
like asphalt streets and crowds and dodging taxis and meeting
chappies at the club and popping in at the Empire for half an
hour and so forth. And there's something about having an
allowance--I don't know . . . sort of makes you chuck your chest
out and feel you're someone. I don't know how to thank you,
gov'nor! You're--you're an absolute sportsman! This is the most
priceless bit of work you've ever done. I feel like a
two-year-old. I don't know when I've felt so braced.
I--I--really, you know, gov'nor, I'm most awfully grateful." "Exactly," said Lord Emsworth. "Ah--precisely. But, Freddie, my
boy," he added, not without pathos, "there is just one thing
more. Do you think that--with an effort--for my sake--you could
endeavor this time not to make a--a damned fool of yourself?" He eyed his offspring wistfully. "Gov'nor," said the Honorable Freddie firmly, "I'll have a jolly
good stab at it!"

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `ESCALATION` (conf: `0.25`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "SOCIAL_EMBARRASSMENT",
  "secondary_mechanisms": [
    "VERBAL_WIT",
    "STATUS_REVERSAL"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Social awkwardness develops through dialogue and shifting interpersonal status."
}
```

---

### Passage 066 [COMPOSITE] — *The Little Nugget* (`the_little_nugget_ch1_07351`)

> Speaker: What | Target Emotion: Calm / Conversational
"he asked," "What is the rate on pigs and on pets? Pigs thirty cents, pets twenty-five," said Morgan.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `ESCALATION` (conf: `0.25`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 8,
  "craft_clarity": 8,
  "training_value": 8,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "The joke is carried primarily by precise ironic phrasing and understatement."
}
```

---

### Passage 067 [COMPOSITE] — *The Man Upstairs* (`the_man_upstairs_ch16_04153`)

> "what do you mean by telling me such nonsense as that? As sure as you drop that beetle I'll break your neck. Look here, Jupiter, do you hear me?," " "You infernal scoundrel!" cried Legrand, apparently much relieved, "Yes, massa, needn't hollo at poor nigger dat style.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "PARTIAL",
  "craft_stratum": "REJECT",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 6,
  "craft_clarity": 4,
  "training_value": 3,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Potential comic premise is present but the supplied fragment does not establish the full mechanism."
}
```

---

### Passage 068 [COMPOSITE] — *Three Men In A Boat* (`three_men_in_a_boat_ch12_01834`)

> CHAPTER XII. Henry VIII. and Anne Boleyn. - Disadvantages of living in same house
with pair of lovers. - A trying time for the English nation. - A
night search for the picturesque. - Homeless and houseless. - [COMPANION_A]
prepares to die. - An angel comes along. - Effect of sudden joy on
[COMPANION_A]. - A little supper. - Lunch. - High price for mustard. - A fearful
battle. - Maidenhead. - Sailing. - Three fishers. - We are cursed. I was sitting on the bank, conjuring up this scene to myself, when
[COMPANION_B] remarked that when I was quite rested, perhaps I would not mind
helping to wash up; and, thus recalled from the days of the glorious
past to the prosaic present, with all its misery and sin, I slid down
into the boat and cleaned out the frying-pan with a stick of wood and a
tuft of grass, polishing it up finally with [COMPANION_B]'s wet shirt. We went over to Magna Charta Island, and had a look at the stone which
stands in the cottage there and on which the great Charter is said to
have been signed; though, as to whether it really was signed there, or,
as some say, on the other bank at "Runningmede," I decline to commit
myself. As far as my own personal opinion goes, however, I am inclined
to give weight to the popular island theory. Certainly, had I been
one of the Barons, at the time, I should have strongly urged upon my
comrades the advisability of our getting such a slippery customer as
King John on to the island, where there was less chance of surprises
and tricks. There are the ruins of an old priory in the grounds of Ankerwyke House,
which is close to Picnic Point, and it was round about the grounds of
this old priory that Henry VIII. is said to have waited for and met
Anne Boleyn. He also used to meet her at Hever Castle in Kent, and also
somewhere near St. Albans. It must have been difficult for the people
of England in those days to have found a spot where these thoughtless
young folk were _not_ spooning. Have you ever been in a house where there are a couple courting? It is
most trying. You think you will go and sit in the drawing-room, and you
march off there. As you open the door, you hear a noise as if somebody
had suddenly recollected something, and, when you get in, Emily is
over by the window, full of interest in the opposite side of the road,
and your friend, John Edward, is at the other end of the room with his
whole soul held in thrall by photographs of other people's relatives. "Oh!" you say, pausing at the door, "I didn't know anybody was here." "Oh! didn't you?" says Emily, coldly, in a tone which implies that she
does not believe you. You hang about for a bit, then you say: "It's very dark. Why don't you light the gas?" John Edward says, "Oh!" he hadn't noticed it; and Emily says that papa
does not like the gas lit in the afternoon. You tell them one or two items of news, and give them your views and
opinions on the Irish question; but this does not appear to interest
them. All they remark on any subject is, "Oh!" "Is it?" "Did he?"
"Yes," and "You don't say so!" And, after ten minutes of such style of
conversation, you edge up to the door, and slip out, and are surprised
to find that the door immediately closes behind you, and shuts itself,
without your having touched it. Half an hour later, you think you will try a pipe in the conservatory.
The only chair in the place is occupied by Emily; and John Edward, if
the language of clothes can be relied upon, has evidently been sitting
on the floor. They do not speak, but they give you a look that says all
that can be said in a civilised community; and you back out promptly
and shut the door behind you. You are afraid to poke your nose into any room in the house now; so,
after walking up and down the stairs for a while, you go and sit in
your own bedroom. This becomes uninteresting, however, after a time,
and so you put on your hat and stroll out into the garden. You walk
down the path, and as you pass the summer-house you glance in, and
there are those two young idiots, huddled up into one corner of it; and
they see you, and are evidently under the idea that, for some wicked
purpose of your own, you are following them about. "Why don't they have a special room for this sort of thing, and make
people keep to it?" you mutter; and you rush back to the hall and get
your umbrella and go out. It must have been much like this when that foolish boy Henry VIII.
was courting his little Anne. People in Buckinghamshire would have
come upon them unexpectedly when they were mooning round Windsor and
Wraysbury, and have exclaimed, "Oh! you here!" and Henry would have
blushed and said, "Yes; he'd just come over to see a man;" and Anne
would have said, "Oh, I'm so glad to see you! Isn't it funny? I've just
met Mr. Henry VIII. in the lane, and he's going the same way I am." Then those people would have gone away and said to themselves: "Oh!
we'd better get out of here while this billing and cooing is on. We'll
go down to Kent." And they would go to Kent, and the first thing they would see in Kent,
when they got there, would be Henry and Anne fooling round Hever Castle. "Oh, drat this!" they would have said. "Here, let's go away. I can't
stand any more of it. Let's go to St. Albans - nice quiet place, St.
Albans." [Picture: River scene] And when they reached St. Albans, there would be that wretched couple,
kissing under the Abbey walls. Then these folks would go and be pirates
until the marriage was over. From Picnic Point to Old Windsor Lock is a delightful bit of the river.
A shady road, dotted here and there with dainty little cottages, runs
by the bank up to the "Bells of Ouseley," a picturesque inn, as most
up-river inns are, and a place where a very good glass of ale may
be drunk - so [COMPANION_A] says; and on a matter of this kind you can take
[COMPANION_A]'s word. Old Windsor is a famous spot in its way. Edward the
Confessor had a palace here, and here the great Earl Godwin was proved
guilty by the justice of that age of having encompassed the death of
the King's brother. Earl Godwin broke a piece of bread and held it in
his hand. "If I am guilty," said the Earl, "may this bread choke me when I eat
it!" Then he put the bread into his mouth and swallowed it, and it choked
him, and he died. After you pass Old Windsor, the river is somewhat uninteresting, and
does not become itself again until you are nearing Boveney. [COMPANION_B] and
I towed up past the Home Park, which stretches along the right bank
from Albert to Victoria Bridge; and as we were passing Datchet, [COMPANION_B]
asked me if I remembered our first trip up the river, and when we
landed at Datchet at ten o'clock at night, and wanted to go to bed. I answered that I did remember it. It will be some time before I forget
it. It was the Saturday before the August Bank Holiday. We were tired and
hungry, we same three, and when we got to Datchet we took out the
hamper, the two bags, and the rugs and coats, and such like things, and
started off to look for diggings. We passed a very pretty little hotel,
with clematis and creeper over the porch; but there was no honeysuckle
about it, and, for some reason or other, I had got my mind fixed on
honeysuckle, and I said: "Oh, don't let's go in there! Let's go on a bit further, and see if
there isn't one with honeysuckle over it." So we went on till we came to another hotel. That was a very nice
hotel, too, and it had honey-suckle on it, round at the side; but
[COMPANION_A] did not like the look of a man who was leaning against the front
door. He said he didn't look a nice man at all, and he wore ugly boots:
so we went on further. We went a goodish way without coming across any
more hotels, and then we met a man, and asked him to direct us to a few. He said: "Why, you are coming away from them. You must turn right round and go
back, and then you will come to the Stag." We said: "Oh, we had been there, and didn't like it - no honeysuckle over it." "Well, then," he said, "there's the Manor House, just opposite. Have
you tried that?" [COMPANION_A] replied that we did not want to go there - didn't like the looks
of a man who was stopping there - [COMPANION_A] did not like the colour of his
hair, didn't like his boots, either. "Well, I don't know what you'll do, I'm sure," said our informant;
"because they are the only two inns in the place." "No other inns!" exclaimed [COMPANION_A]. "None," replied the man. "What on earth are we to do?" cried [COMPANION_A]. Then [COMPANION_B] spoke up. He said [COMPANION_A] and I could get an hotel built for
us, if we liked, and have some people made to put in. For his part, he
was going back to the Stag. The greatest minds never realise their ideals in any matter; and [COMPANION_A]
and I sighed over the hollowness of all earthly desires, and followed
[COMPANION_B]. We took our traps into the Stag, and laid them down in the hall. The landlord came up and said: "Good evening, gentlemen." "Oh, good evening," said [COMPANION_B]; "we want three beds, please." "Very sorry, sir," said the landlord; "but I'm afraid we can't manage
it." "Oh, well, never mind," said [COMPANION_B], "two will do. Two of us can sleep
in one bed, can't we?" he continued, turning to [COMPANION_A] and me. [COMPANION_A] said, "Oh, yes;" he thought [COMPANION_B] and I could sleep in one bed
very easily. "Very sorry, sir," again repeated the landlord: "but we really haven't
got a bed vacant in the whole house. In fact, we are putting two, and
even three gentlemen in one bed, as it is." This staggered us for a bit. But [COMPANION_A], who is an old traveller, rose to the occasion, and,
laughing cheerily, said: "Oh, well, we can't help it. We must rough it. You must give us a
shake-down in the billiard-room." "Very sorry, sir. Three gentlemen sleeping on the billiard-table
already, and two in the coffee-room. Can't possibly take you in
to-night." We picked up our things, and went over to the Manor House. It was a
pretty little place. I said I thought I should like it better than the
other house; and [COMPANION_A] said, "Oh, yes," it would be all right, and we
needn't look at the man with the red hair; besides, the poor fellow
couldn't help having red hair. [COMPANION_A] spoke quite kindly and sensibly about it. The people at the Manor House did not wait to hear us talk. The
landlady met us on the doorstep with the greeting that we were the
fourteenth party she had turned away within the last hour and a half.
As for our meek suggestions of stables, billiard-room, or coal-cellars,
she laughed them all to scorn: all these nooks had been snatched up
long ago. Did she know of any place in the whole village where we could get
shelter for the night? "Well, if we didn't mind roughing it - she did not recommend it, mind - but
there was a little beershop half a mile down the Eton road - " We waited to hear no more; we caught up the hamper and the bags, and
the coats and rugs, and parcels, and ran. The distance seemed more like
a mile than half a mile, but we reached the place at last, and rushed,
panting, into the bar. The people at the beershop were rude. They merely laughed at us.
There were only three beds in the whole house, and they had seven
single gentlemen and two married couples sleeping there already. A
kind-hearted bargeman, however, who happened to be in the tap-room,
thought we might try the grocer's, next door to the Stag, and we went
back. The grocer's was full. An old woman we met in the shop then kindly took
us along with her for a quarter of a mile, to a lady friend of hers,
who occasionally let rooms to gentlemen. This old woman walked very slowly, and we were twenty minutes getting
to her lady friend's. She enlivened the journey by describing to us, as
we trailed along, the various pains she had in her back. Her lady friend's rooms were let. From there we were recommended to No.
27. No. 27 was full, and sent us to No. 32, and 32 was full. Then we went back into the high road, and [COMPANION_A] sat down on the hamper
and said he would go no further. He said it seemed a quiet spot, and he
would like to die there. He requested [COMPANION_B] and me to kiss his mother
for him, and to tell all his relations that he forgave them and died
happy. At that moment an angel came by in the disguise of a small boy (and
I cannot think of any more effective disguise an angel could have
assumed), with a can of beer in one hand, and in the other something
at the end of a string, which he let down on to every flat stone he
came across, and then pulled up again, this producing a peculiarly
unattractive sound, suggestive of suffering. We asked this heavenly messenger (as we discovered him afterwards to
be) if he knew of any lonely house, whose occupants were few and feeble
(old ladies or paralysed gentlemen preferred), who could be easily
frightened into giving up their beds for the night to three desperate
men; or, if not this, could he recommend us to an empty pigstye, or a
disused limekiln, or anything of that sort. He did not know of any such
place - at least, not one handy; but he said that, if we liked to come
with him, his mother had a room to spare, and could put us up for the
night. We fell upon his neck there in the moonlight and blessed him, and it
would have made a very beautiful picture if the boy himself had not
been so over-powered by our emotion as to be unable to sustain himself
under it, and sunk to the ground, letting us all down on top of him.
[COMPANION_A] was so overcome with joy that he fainted, and had to seize the
boy's beer-can and half empty it before he could recover consciousness,
and then he started off at a run, and left [COMPANION_B] and me to bring on
the luggage. It was a little four-roomed cottage where the boy lived, and his
mother - good soul! - gave us hot bacon for supper, and we ate it all - five
pounds - and a jam tart afterwards, and two pots of tea, and then we went
to bed. There were two beds in the room; one was a 2ft. 6in. truckle
bed, and [COMPANION_B] and I slept in that, and kept in by tying ourselves
together with a sheet; and the other was the little boy's bed, and
[COMPANION_A] had that all to himself, and we found him, in the morning, with
two feet of bare leg sticking out at the bottom, and [COMPANION_B] and I used
it to hang the towels on while we bathed. We were not so uppish about what sort of hotel we would have, next time
we went to Datchet. To return to our present trip: nothing exciting happened, and we tugged
steadily on to a little below Monkey Island, where we drew up and
lunched. We tackled the cold beef for lunch, and then we found that we
had forgotten to bring any mustard. I don't think I ever in my life,
before or since, felt I wanted mustard as badly as I felt I wanted it
then. I don't care for mustard as a rule, and it is very seldom that I
take it at all, but I would have given worlds for it then. I don't know how many worlds there may be in the universe, but anyone
who had brought me a spoonful of mustard at that precise moment could
have had them all. I grow reckless like that when I want a thing and
can't get it. [COMPANION_A] said he would have given worlds for mustard too. It would have
been a good thing for anybody who had come up to that spot with a can
of mustard, then: he would have been set up in worlds for the rest of
his life. But there! I daresay both [COMPANION_A] and I would have tried to back out of
the bargain after we had got the mustard. One makes these extravagant
offers in moments of excitement, but, of course, when one comes to
think of it, one sees how absurdly out of proportion they are with the
value of the required article. I heard a man, going up a mountain in
Switzerland, once say he would give worlds for a glass of beer, and,
when he came to a little shanty where they kept it, he kicked up a most
fearful row because they charged him five francs for a bottle of Bass.
He said it was a scandalous imposition, and he wrote to the _Times_
about it. It cast a gloom over the boat, there being no mustard. We ate our beef
in silence. Existence seemed hollow and uninteresting. We thought
of the happy days of childhood, and sighed. We brightened up a bit,
however, over the apple-tart, and, when [COMPANION_B] drew out a tin of
pine-apple from the bottom of the hamper, and rolled it into the middle
of the boat, we felt that life was worth living after all. We are very fond of pine-apple, all three of us. We looked at the
picture on the tin; we thought of the juice. We smiled at one another,
and [COMPANION_A] got a spoon ready. Then we looked for the knife to open the tin with. We turned out
everything in the hamper. We turned out the bags. We pulled up the
boards at the bottom of the boat. We took everything out on to the bank
and shook it. There was no tin-opener to be found. Then [COMPANION_A] tried to open the tin with a pocket-knife, and broke the
knife and cut himself badly; and [COMPANION_B] tried a pair of scissors, and
the scissors flew up, and nearly put his eye out. While they were
dressing their wounds, I tried to make a hole in the thing with the
spiky end of the hitcher, and the hitcher slipped and jerked me out
between the boat and the bank into two feet of muddy water, and the tin
rolled over, uninjured, and broke a teacup. Then we all got mad. We took that tin out on the bank, and [COMPANION_A] went
up into a field and got a big sharp stone, and I went back into the
boat and brought out the mast, and [COMPANION_B] held the tin and [COMPANION_A] held
the sharp end of his stone against the top of it, and I took the mast
and poised it high up in the air, and gathered up all my strength and
brought it down. It was [COMPANION_B]'s straw hat that saved his life that day. He keeps that
hat now (what is left of it), and, of a winter's evening, when the
pipes are lit and the boys are telling stretchers about the dangers
they have passed through, [COMPANION_B] brings it down and shows it round, and
the stirring tale is told anew, with fresh exaggerations every time. [COMPANION_A] got off with merely a flesh wound. After that, I took the tin off myself, and hammered at it with the mast
till I was worn out and sick at heart, whereupon [COMPANION_A] took it in hand. [Picture: Flattened tin] We beat it out flat; we beat it back square;
we battered it into every form known to geometry - but we could not make
a hole in it. Then [COMPANION_B] went at it, and knocked it into a shape, so
strange, so weird, so unearthly in its wild hideousness, that he got
frightened and threw away the mast. Then we all three sat round it on
the grass and looked at it. There was one great dent across the top that had the appearance of a
mocking grin, and it drove us furious, so that [COMPANION_A] rushed at the
thing, and caught it up, and flung it far into the middle of the river,
and as it sank we hurled our curses at it, and we got into the boat and
rowed away from the spot, and never paused till we reached Maidenhead. Maidenhead itself is too snobby to be pleasant. It is the haunt of
the river swell and his overdressed female companion. It is the
town of showy hotels, patronised chiefly by dudes and ballet girls.
It is the witch's kitchen from which go forth those demons of the
river - steam-launches. The _London Journal_ duke always has his "little
place" at Maidenhead; and the heroine of the three-volume novel always
dines there when she goes out on the spree with somebody else's husband. [Picture: River scene] We went through Maidenhead quickly, and then eased up, and took
leisurely that grand reach beyond Boulter's and Cookham locks.
Clieveden Woods still wore their dainty dress of spring, and rose
up, from the water's edge, in one long harmony of blended shades of
fairy green. In its unbroken loveliness this is, perhaps, the sweetest
stretch of all the river, and lingeringly we slowly drew our little
boat away from its deep peace. We pulled up in the backwater, just below Cookham, and had tea; and,
when we were through the lock, it was evening. A stiffish breeze had
sprung up - in our favour, for a wonder; for, as a rule on the river,
the wind is always dead against you whatever way you go. It is against
you in the morning, when you start for a day's trip, and you pull a
long distance, thinking how easy it will be to come back with the sail.
Then, after tea, the wind veers round, and you have to pull hard in its
teeth all the way home. When you forget to take the sail at all, then the wind is consistently
in your favour both ways. But there! this world is only a probation,
and man was born to trouble as the sparks fly upward. This evening, however, they had evidently made a mistake, and had put
the wind round at our back instead of in our face. We kept very quiet
about it, and got the sail up quickly before they found it out, and
then we spread ourselves about the boat in thoughtful attitudes, and
the sail bellied out, and strained, and grumbled at the mast, and the
boat flew. I steered. There is no more thrilling sensation I know of than sailing. It comes
as near to flying as man has got to yet - except in dreams. The wings of
the rushing wind seem to be bearing you onward, you know not where.
You are no longer the slow, plodding, puny thing of clay, creeping
tortuously upon the ground; you are a part of Nature! Your heart is
throbbing against hers! Her glorious arms are round you, raising you
up against her heart! Your spirit is at one with hers; your limbs
grow light! The voices of the air are singing to you. The earth seems
far away and little; and the clouds, so close above your head, are
brothers, and you stretch your arms to them. We had the river to ourselves, except that, far in the distance,
we could see a fishing-punt, moored in mid-stream, on which three
fishermen sat; and we skimmed over the water, and passed the wooded
banks, and no one spoke. I was steering. As we drew nearer, we could see that the three men fishing seemed
old and solemn-looking men. They sat on three chairs in the punt,
and watched intently their lines. And the red sunset threw a mystic
light upon the waters, and tinged with fire the towering woods, and
made a golden glory of the piled-up clouds. It was an hour of deep
enchantment, of ecstatic hope and longing. The little sail stood out
against the purple sky, the gloaming lay around us, wrapping the world
in rainbow shadows; and, behind us, crept the night. We seemed like knights of some old legend, sailing across some mystic
lake into the unknown realm of twilight, unto the great land of the
sunset. We did not go into the realm of twilight; we went slap into that punt,
where those three old men were fishing. We did not know what had
happened at first, because the sail shut out the view, but from the
nature of the language that rose up upon the evening air, we gathered
that we had come into the neighbourhood of human beings, and that they
were vexed and discontented. [COMPANION_A] let the sail down, and then we saw what had happened. We had
knocked those three old gentlemen off their chairs into a general
heap at the bottom of the boat, and they were now slowly and
painfully sorting themselves out from each other, and picking fish
off themselves; and as they worked, they cursed us - not with a common
cursory curse, but with long, carefully-thought-out, comprehensive
curses, that embraced the whole of our career, and went away into the
distant future, and included all our relations, and covered everything
connected with us - good, substantial curses. [COMPANION_A] told them they ought to be grateful for a little excitement,
sitting there fishing all day, and he also said that he was shocked and
grieved to hear men their age give way to temper so. But it did not do any good. [COMPANION_B] said he would steer, after that. He said a mind like mine ought
not to be expected to give itself away in steering boats - better let a
mere commonplace human being see after that boat, before we jolly well
all got drowned; and he took the lines, and brought us up to Marlow. And at Marlow we left the boat by the bridge, and went and put up for
the night at
 the "Crown." [Picture: The boat]

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `SOCIAL_EMBARRASSMENT` (conf: `0.5`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [
    "PHYSICAL_COMPLICATION",
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Repeated complications accumulate into farce with restrained narration."
}
```

---

### Passage 069 [COMPOSITE] — *Three Men On The Bummel* (`three_men_on_the_bummel_ch8_03993`)

> "If [COMPANION_B] is not in the secret of this thing," said [COMPANION_A]--we were
walking by ourselves for an hour, he having remained behind in the hotel
to write a letter to his aunt,--"if he has not observed these statues,
then by their aid we will make a better and a thinner man of him, and
that this very evening.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 5,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Serious/expository passage; no sufficiently clear comic mechanism."
}
```

---

### Passage 070 [COMPOSITE] — *A Damsel In Distress* (`a_damsel_in_distress_ch17_10280`)

> CHAPTER XIV LORD WISBEACH Jimmy halted in his tracks. The apparition had startled him. He
had been thinking of Ann, but he had not expected her to bound
out at him, waving her arms. "What's the matter?" he enquired. Ann pulled him towards a side-street. "You mustn't go to the house. Everything has gone wrong." "Everything gone wrong? I thought I had made a hit. I have with
your uncle, anyway. We parted on the friendliest terms. We have
arranged to go to the ball-game together to-morrow. He is going
to tell them at the office that Carnegie wants to see him." "It isn't uncle Peter. It's aunt Nesta." "Ah, there you touch my conscience. I was a little tactless, I'm
afraid, with Ogden. It happened before you came into the room. I
suppose that is the trouble?" "It has nothing do with that," said Ann impatiently. "It's much
worse. Aunt Nesta is suspicious. She has guessed that you aren't
really Jimmy Crocker." "Great Scott! How?" "I tried to calm her down, but she still suspects. So now she has
decided to wait and see if Skinner, the butler, knows you. If he
doesn't, she will know that she was right." Jimmy was frankly puzzled. "I don't quite follow the reasoning. Surely it's a peculiar kind
of test. Why should she think a man cannot be honest and true
unless her butler knows him? There must be hundreds of worthy
citizens whom he does not know." "Skinner arrived from England a few days ago. Until then he was
employed by Mrs. Crocker. Now do you understand?" Jimmy stopped. She had spoken slowly and distinctly, and there
could be no possibility that he had misunderstood her, yet he
scarcely believed that he had heard her aright. How could a man
named Skinner have been his step-mother's butler? Bayliss had
been with the family ever since they had arrived in London. "Are you sure?" "Of course, of course I'm sure. Aunt Nesta told me herself. There
can't possibly be a mistake, because it was Skinner who let her
in when she called on Mrs. Crocker. Uncle Peter told me about it.
He had a talk with the man in the hall and found that he was a
baseball enthusiast--" A wild, impossible idea flashed upon Jimmy. It was so absurd that
he felt ashamed of entertaining it even for a moment. But strange
things were happening these times, and it might be . . . "What sort of looking man is Skinner?" "Oh, stout, clean-shaven. I like him. He's much more human than I
thought butlers ever were. Why?" "Oh, nothing." "Of course, you can't go back to the house. You see that? He
would say that you aren't Jimmy Crocker and then you would be
arrested." "I don't see that. If I am sufficiently like Crocker for his
friends to mistake me for him in restaurants, why shouldn't this
butler mistake me, too?" "But--?" "And, consider. In any case, there's no harm done. If he fails to
recognise me when he opens the door to us, we shall know that the
game is up: and I shall have plenty of time to disappear. If the
likeness deceives him, all will be well. I propose that we go to
the house, ring the bell, and when he appears, I will say 'Ah,
Skinner! Honest fellow!' or words to that effect. He will either
stare blankly at me or fawn on me like a faithful watchdog. We
will base our further actions on which way the butler jumps." The sound of the bell died away. Footsteps were heard. Ann
reached for Jimmy's arm and--clutched it. "Now!" she whispered. The door opened. Next moment Jimmy's suspicion was confirmed.
Gaping at them from the open doorway, wonderfully respectable and
butlerlike in swallow-tails, stood his father. How he came to be
there, and why he was there, Jimmy did not know. But there he
was. Jimmy had little faith in his father's talents as a man of
discretion. The elder Crocker was one of those simple, straight
forward people who, when surprised, do not conceal their
surprise, and who, not understanding any situation in which they
find themselves, demand explanation on the spot. Swift and
immediate action was indicated on his part before his amazed
parent, finding him on the steps of the one house in New York
where he was least likely to be, should utter words that would
undo everything. He could see the name Jimmy trembling on Mr.
Crocker's lips. He waved his hand cheerily. "Ah, Skinner, there you are!" he said breezily. "Miss Chester was
telling me that you had left my step-mother. I suppose you sailed
on the boat before mine. I came over on the _Caronia_. I suppose
you didn't expect to see me again so soon, eh?" A spasm seemed to pass over Mr. Crocker's face, leaving it calm
and serene. He had been thrown his cue, and like the old actor he
was he took it easily and without confusion. He smiled a
respectful smile. "No, indeed, sir." He stepped aside to allow them to enter. Jimmy caught Ann's eye
as she passed him. It shone with relief and admiration, and it
exhilarated Jimmy like wine. As she moved towards the stairs, he
gave expression to his satisfaction by slapping his father on the
back with a report that rang out like a pistol shot. "What was that?" said Ann, turning. "Something out on the Drive, I think," said Jimmy. "A car
back-firing, I fancy, Skinner." "Very probably, sir." He followed Ann to the stairs. As he started to mount them, a
faint whisper reached his ears. "'At-a-boy!" It was Mr. Crocker's way of bestowing a father's blessing. Ann walked into the drawing-room, her head high, triumph in the
glance which she cast upon her unconscious aunt. "Quite an interesting little scene downstairs, aunt Nesta," she
said. "The meeting of the faithful old retainer and the young
master. Skinner was almost overcome with surprise and joy when he
saw Jimmy!" Mrs. Pett could not check an incautious exclamation. "Did Skinner recognise--?" she began; then stopped herself
abruptly. Ann laughed. "Did he recognise Jimmy? Of course! He was hardly likely to have
forgotten him, surely? It isn't much more than a week since he
was waiting on him in London." "It was a very impressive meeting," said Jimmy. "Rather like the
reunion of Ulysses and the hound Argos, of which this bright-eyed
child here--" he patted Ogden on the head, a proceeding violently
resented by that youth--"has no doubt read in the course of his
researches into the Classics. I was Ulysses, Skinner enacted the
role of the exuberant dog." Mrs. Pett was not sure whether she was relieved or disappointed
at this evidence that her suspicions had been without foundation.
On the whole, relief may be said to have preponderated. "I have no doubt he was pleased to see you again. He must have
been very much astonished." "He was!" "You will be meeting another old friend in a minute or two," said
Mrs. Pett. Jimmy had been sinking into a chair. This remark stopped him in
mid-descent. "Another!" Mrs. Pett glanced at the clock. "Lord Wisbeach is coming to lunch." "Lord Wisbeach!" cried Ann. "He doesn't know Jimmy." "Eugenia informed me in London that he was one of your best
friends, James." Ann looked helplessly at Jimmy. She was conscious again of that
feeling of not being able to cope with Fate's blows, of not
having the strength to go on climbing over the barriers which
Fate placed in her path. Jimmy, for his part, was cursing the ill fortune that had brought
Lord Wisbeach across his path. He saw clearly that it only needed
recognition by one or two more intimates of Jimmy Crocker to make
Ann suspect his real identity. The fact that she had seen him
with Bayliss in Paddington Station and had fallen into the error
of supposing Bayliss to be his father had kept her from
suspecting until now; but this could not last forever. He
remembered Lord Wisbeach well, as a garrulous, irrepressible
chatterer who would probably talk about old times to such an
extent as to cause Ann to realise the truth in the first five
minutes. The door opened. "Lord Wisbeach," announced Mr. Crocker. "I'm afraid I'm late, Mrs. Pett," said his lordship. "No. You're quite punctual. Lord Wisbeach, here is an old friend
of yours, James Crocker." There was an almost imperceptible pause. Then Jimmy stepped
forward and held out his hand. "Hello, Wizzy, old man!" "H-hello, Jimmy!" Their eyes met. In his lordship's there was an expression of
unmistakable relief, mingled with astonishment. His face, which
had turned a sickly white, flushed as the blood poured back into
it. He had the appearance of a man who had had a bad shock and is
just getting over it. Jimmy, eyeing him curiously, was not
surprised at his emotion. What the man's game might be, he could
not say; but of one thing he was sure, which was that this was
not Lord Wisbeach, but--on the contrary--some one he had never
seen before in his life. "Luncheon is served, madam!" said Mr. Crocker sonorously from the
doorway.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `ESCALATION` (conf: `0.98`)
- **Temporal Horizon:** `LOCAL` | Secondary: `['MISUNDERSTANDING']`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "STATUS_REVERSAL",
  "secondary_mechanisms": [
    "VERBAL_WIT",
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "A character expected to occupy one social position ends up controlling or correcting the other."
}
```

---

### Passage 071 [COMPOSITE] — *My Man Jeeves* (`my_man_jeeves_ch7_03131`)

> "I refuse to be badgered by reporters. There were a number of adhesive young men who endeavoured to elicit from me my views on America while the boat was approaching the dock. I will not be subjected to this persecution again," "There will be no reporters among them?" "Reporters? Rather not! Why?" "That'll be absolutely all right, uncle.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 8,
  "craft_clarity": 9,
  "training_value": 8,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Literal misreading of a situation generates the central comic turn."
}
```

---

### Passage 072 [COMPOSITE] — *Right Ho* (`right_ho_ch12_08174`)

> "My dear [COMPANION_B] - I shall be seeing you to-morrow, I hope; but I think it is better, before we meet, to prepare you for a curious situation that has arisen in connection with the legacy which your father inherited from your Aunt Emily, and which you are expecting me, as trustee, to hand over to you, now that you have reached your twenty-fifth birthday. You have doubtless heard your father speak of your twin-brother Alfred, who was lost or kidnapped - which, was never ascertained - when you were both babies. When no news was received of him for so many years, it was supposed that he was dead. Yesterday, however, I received a letter purporting that he had been living all this time in Buenos Ayres as the adopted son of a wealthy South American, and has only recently discovered his identity. He states that he is on his way to meet me, and will arrive any day now. Of course, like other claimants, he may prove to be an impostor, but meanwhile his intervention will, I fear, cause a certain delay before I can hand over your money to you. It will be necessary to go into a thorough examination of credentials, etc., and this will take some time. But I will go fully into the matter with you when we meet. - Your affectionate uncle," This is how it ran: AUGUSTUS ARBUTT.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.25`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "PARTIAL",
  "craft_stratum": "REJECT",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 7,
  "craft_clarity": 4,
  "training_value": 4,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Some witty language, but insufficient structure for a reliable training example."
}
```

---

### Passage 073 [COMPOSITE] — *Something Fresh* (`something_fresh_ch9_00226`)

> Speaker: Character | Target Emotion: Calm / Conversational
"what I wish to do is to break open this closet," "So," said the Efficient Baxter, cutting in on the flow of
speech,.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [
    "MISUNDERSTANDING",
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "The same comic premise is repeatedly intensified through new complications."
}
```

---

### Passage 074 [COMPOSITE] — *The Little Nugget* (`the_little_nugget_ch1_05664`)

> "across it and mailed it to Morgan. Morgan returned it asking for explanation. Flannery replied:," Some months later, in desperation, he seized a sheet of paper and wrote "160 There be now one hundred sixty of them dago pigs, for heavens sake let me sell off some, do you want me to go crazy, what.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 6,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Narrative exposition rather than transferable comic craft."
}
```

---

### Passage 075 [COMPOSITE] — *The Man Upstairs* (`the_man_upstairs_ch31_05927`)

> "there is omnipotence in the cause that changed the views of a man like Carwin. The divinity that shielded me from his attempts will take suitable care of my future safety. Thus to yield to my fears is to deserve that they should be real," Else why that startling entreaty to refrain from opening the closet? By what inexplicable infatuation was I compelled to proceed? "Surely," said I, Scarcely had I uttered these words, when my attention was startled by the sound of footsteps.

- **Detector Prediction:** `YES` | Stratum: `COMPOSITE_CRAFT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "DEADPAN_REACTION",
  "secondary_mechanisms": [
    "ESCALATION",
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Absurd events are narrated with restraint while the underlying situation keeps becoming worse."
}
```

---

### Passage 076 [PARTIAL] — *A Damsel In Distress* (`a_damsel_in_distress_ch6_07831`)

> Speaker: Character | Target Emotion: Calm / Conversational
"I only arrived in London yesterday," said the girl, "and I
haven't got used to your keeping-to-the-left rules.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "SOCIAL_EMBARRASSMENT",
  "secondary_mechanisms": [
    "STATUS_REVERSAL"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 8,
  "craft_clarity": 8,
  "training_value": 8,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "The comedy comes from a character's increasingly uncomfortable public/social position."
}
```

---

### Passage 077 [PARTIAL] — *Idle Thoughts* (`idle_thoughts_ch1_00946`)

> THE IMPORTANCE OF BEING EARNEST: A TRIVIAL COMEDY FOR SERIOUS PEOPLE *** The Importance of Being Earnest A Trivial Comedy for Serious People THE PERSONS IN THE PLAY John Worthing, J.P. Algernon Moncrieff Rev. Canon Chasuble, D.D. Merriman, Butler Lane, Manservant Lady Bracknell Hon. Gwendolen Fairfax Cecily Cardew Miss Prism, Governess THE SCENES OF THE PLAY ACT I. Algernon Moncrieff's Flat in Half-Moon Street, W. ACT II. The Garden at the Manor House, Woolton. ACT III. Drawing-Room at the Manor House, Woolton. TIME: The Present. LONDON: ST. JAMES'S THEATRE Lessee and Manager: Mr. [COMPANION_B] Alexander February 14th, 1895 * * * * * John Worthing, J.P.: Mr. [COMPANION_B] Alexander. Algernon Moncrieff: Mr. Allen Aynesworth. Rev. Canon Chasuble, D.D.: Mr. H. H. Vincent. Merriman: Mr. Frank Dyall. Lane: Mr. F. Kinsey Peile. Lady Bracknell: Miss Rose Leclercq. Hon. Gwendolen Fairfax: Miss Irene Vanbrugh. Cecily Cardew: Miss Evelyn Millard. Miss Prism: Mrs. [COMPANION_B] Canninge. FIRST ACT SCENE Morning-room in Algernon's flat in Half-Moon Street. The room is luxuriously and artistically furnished. The sound of a piano is heard in the adjoining room. [Lane is arranging afternoon tea on the table, and after the music has ceased, Algernon enters.] ALGERNON. Did you hear what I was playing, Lane? LANE. I didn't think it polite to listen, sir. ALGERNON. I'm sorry for that, for your sake. I don't play accurately - any one can play accurately - but I play with wonderful expression. As far as the piano is concerned, sentiment is my forte. I keep science for Life. LANE. Yes, sir. ALGERNON. And, speaking of the science of Life, have you got the cucumber sandwiches cut for Lady Bracknell? LANE. Yes, sir. [Hands them on a salver.] ALGERNON. [Inspects them, takes two, and sits down on the sofa.] Oh! . . . by the way, Lane, I see from your book that on Thursday night, when Lord Shoreman and Mr. Worthing were dining with me, eight bottles of champagne are entered as having been consumed. LANE. Yes, sir; eight bottles and a pint. ALGERNON. Why is it that at a bachelor's establishment the servants invariably drink the champagne? I ask merely for information. LANE. I attribute it to the superior quality of the wine, sir. I have often observed that in married households the champagne is rarely of a first-rate brand. ALGERNON. Good heavens! Is marriage so demoralising as that? LANE. I believe it _is_ a very pleasant state, sir. I have had very little experience of it myself up to the present. I have only been married once. That was in consequence of a misunderstanding between myself and a young person. ALGERNON. [Languidly_._] I don't know that I am much interested in your family life, Lane. LANE. No, sir; it is not a very interesting subject. I never think of it myself. ALGERNON. Very natural, I am sure. That will do, Lane, thank you. LANE. Thank you, sir. [Lane goes out.] ALGERNON. Lane's views on marriage seem somewhat lax. Really, if the lower orders don't set us a good example, what on earth is the use of them? They seem, as a class, to have absolutely no sense of moral responsibility. [Enter Lane.] LANE. Mr. Ernest Worthing. [Enter Jack.] [Lane goes out_._] ALGERNON. How are you, my dear Ernest? What brings you up to town? JACK. Oh, pleasure, pleasure! What else should bring one anywhere? Eating as usual, I see, Algy! ALGERNON. [Stiffly_._] I believe it is customary in good society to take some slight refreshment at five o'clock. Where have you been since last Thursday? JACK. [Sitting down on the sofa.] In the country. ALGERNON. What on earth do you do there? JACK. [Pulling off his gloves_._] When one is in town one amuses oneself. When one is in the country one amuses other people. It is excessively boring. ALGERNON. And who are the people you amuse? JACK. [Airily_._] Oh, neighbours, neighbours. ALGERNON. Got nice neighbours in your part of Shropshire? JACK. Perfectly horrid! Never speak to one of them. ALGERNON. How immensely you must amuse them! [Goes over and takes sandwich.] By the way, Shropshire is your county, is it not? JACK. Eh? Shropshire? Yes, of course. Hallo! Why all these cups? Why cucumber sandwiches? Why such reckless extravagance in one so young? Who is coming to tea? ALGERNON. Oh! merely Aunt Augusta and Gwendolen. JACK. How perfectly delightful! ALGERNON. Yes, that is all very well; but I am afraid Aunt Augusta won't quite approve of your being here. JACK. May I ask why? ALGERNON. My dear fellow, the way you flirt with Gwendolen is perfectly disgraceful. It is almost as bad as the way Gwendolen flirts with you. JACK. I am in love with Gwendolen. I have come up to town expressly to propose to her. ALGERNON. I thought you had come up for pleasure? . . . I call that business. JACK. How utterly unromantic you are! ALGERNON. I really don't see anything romantic in proposing. It is very romantic to be in love. But there is nothing romantic about a definite proposal. Why, one may be accepted. One usually is, I believe. Then the excitement is all over. The very essence of romance is uncertainty. If ever I get married, I'll certainly try to forget the fact. JACK. I have no doubt about that, dear Algy. The Divorce Court was specially invented for people whose memories are so curiously constituted. ALGERNON. Oh! there is no use speculating on that subject. Divorces are made in Heaven - [Jack puts out his hand to take a sandwich. Algernon at once interferes.] Please don't touch the cucumber sandwiches. They are ordered specially for Aunt Augusta. [Takes one and eats it.] JACK. Well, you have been eating them all the time. ALGERNON. That is quite a different matter. She is my aunt. [Takes plate from below.] Have some bread and butter. The bread and butter is for Gwendolen. Gwendolen is devoted to bread and butter. JACK. [Advancing to table and helping himself.] And very good bread and butter it is too. ALGERNON. Well, my dear fellow, you need not eat as if you were going to eat it all. You behave as if you were married to her already. You are not married to her already, and I don't think you ever will be. JACK. Why on earth do you say that? ALGERNON. Well, in the first place girls never marry the men they flirt with. Girls don't think it right. JACK. Oh, that is nonsense! ALGERNON. It isn't. It is a great truth. It accounts for the extraordinary number of bachelors that one sees all over the place. In the second place, I don't give my consent. JACK. Your consent! ALGERNON. My dear fellow, Gwendolen is my first cousin. And before I allow you to marry her, you will have to clear up the whole question of Cecily. [Rings bell.] JACK. Cecily! What on earth do you mean? What do you mean, Algy, by Cecily! I don't know any one of the name of Cecily. [Enter Lane.] ALGERNON. Bring me that cigarette case Mr. Worthing left in the smoking-room the last time he dined here. LANE. Yes, sir. [Lane goes out.] JACK. Do you mean to say you have had my cigarette case all this time? I wish to goodness you had let me know. I have been writing frantic letters to Scotland Yard about it. I was very nearly offering a large reward. ALGERNON. Well, I wish you would offer one. I happen to be more than usually hard up. JACK. There is no good offering a large reward now that the thing is found. [Enter Lane with the cigarette case on a salver. Algernon takes it at once. Lane goes out.] ALGERNON. I think that is rather mean of you, Ernest, I must say. [Opens case and examines it.] However, it makes no matter, for, now that I look at the inscription inside, I find that the thing isn't yours after all. JACK. Of course it's mine. [Moving to him.] You have seen me with it a hundred times, and you have no right whatsoever to read what is written inside. It is a very ungentlemanly thing to read a private cigarette case. ALGERNON. Oh! it is absurd to have a hard and fast rule about what one should read and what one shouldn't. More than half of modern culture depends on what one shouldn't read. JACK. I am quite aware of the fact, and I don't propose to discuss modern culture. It isn't the sort of thing one should talk of in private. I simply want my cigarette case back. ALGERNON. Yes; but this isn't your cigarette case. This cigarette case is a present from some one of the name of Cecily, and you said you didn't know any one of that name. JACK. Well, if you want to know, Cecily happens to be my aunt. ALGERNON. Your aunt! JACK. Yes. Charming old lady she is, too. Lives at Tunbridge Wells. Just give it back to me, Algy. ALGERNON. [Retreating to back of sofa.] But why does she call herself little Cecily if she is your aunt and lives at Tunbridge Wells? [Reading.] 'From little Cecily with her fondest love.' JACK. [Moving to sofa and kneeling upon it.] My dear fellow, what on earth is there in that? Some aunts are tall, some aunts are not tall. That is a matter that surely an aunt may be allowed to decide for herself. You seem to think that every aunt should be exactly like your aunt! That is absurd! For Heaven's sake give me back my cigarette case. [Follows Algernon round the room.] ALGERNON. Yes. But why does your aunt call you her uncle? 'From little Cecily, with her fondest love to her dear Uncle Jack.' There is no objection, I admit, to an aunt being a small aunt, but why an aunt, no matter what her size may be, should call her own nephew her uncle, I can't quite make out. Besides, your name isn't Jack at all; it is Ernest. JACK. It isn't Ernest; it's Jack. ALGERNON. You have always told me it was Ernest. I have introduced you to every one as Ernest. You answer to the name of Ernest. You look as if your name was Ernest. You are the most earnest-looking person I ever saw in my life. It is perfectly absurd your saying that your name isn't Ernest. It's on your cards. Here is one of them. [Taking it from case.] 'Mr. Ernest Worthing, B. 4, The Albany.' I'll keep this as a proof that your name is Ernest if ever you attempt to deny it to me, or to Gwendolen, or to any one else. [Puts the card in his pocket.] JACK. Well, my name is Ernest in town and Jack in the country, and the cigarette case was given to me in the country. ALGERNON. Yes, but that does not account for the fact that your small Aunt Cecily, who lives at Tunbridge Wells, calls you her dear uncle. Come, old boy, you had much better have the thing out at once. JACK. My dear Algy, you talk exactly as if you were a dentist. It is very vulgar to talk like a dentist when one isn't a dentist. It produces a false impression. ALGERNON. Well, that is exactly what dentists always do. Now, go on! Tell me the whole thing. I may mention that I have always suspected you of being a confirmed and secret Bunburyist; and I am quite sure of it now. JACK. Bunburyist? What on earth do you mean by a Bunburyist? ALGERNON. I'll reveal to you the meaning of that incomparable expression as soon as you are kind enough to inform me why you are Ernest in town and Jack in the country. JACK. Well, produce my cigarette case first. ALGERNON. Here it is. [Hands cigarette case.] Now produce your explanation, and pray make it improbable. [Sits on sofa.] JACK. My dear fellow, there is nothing improbable about my explanation at all. In fact it's perfectly ordinary. Old Mr. Thomas Cardew, who adopted me when I was a little boy, made me in his will guardian to his grand-daughter, Miss Cecily Cardew. Cecily, who addresses me as her uncle from motives of respect that you could not possibly appreciate, lives at my place in the country under the charge of her admirable governess, Miss Prism. ALGERNON. Where is that place in the country, by the way? JACK. That is nothing to you, dear boy. You are not going to be invited . . . I may tell you candidly that the place is not in Shropshire. ALGERNON. I suspected that, my dear fellow! I have Bunburyed all over Shropshire on two separate occasions. Now, go on. Why are you Ernest in town and Jack in the country? JACK. My dear Algy, I don't know whether you will be able to understand my real motives. You are hardly serious enough. When one is placed in the position of guardian, one has to adopt a very high moral tone on all subjects. It's one's duty to do so. And as a high moral tone can hardly be said to conduce very much to either one's health or one's happiness, in order to get up to town I have always pretended to have a younger brother of the name of Ernest, who lives in the Albany, and gets into the most dreadful scrapes. That, my dear Algy, is the whole truth pure and simple. ALGERNON. The truth is rarely pure and never simple. Modern life would be very tedious if it were either, and modern literature a complete impossibility! JACK. That wouldn't be at all a bad thing. ALGERNON. Literary criticism is not your forte, my dear fellow. Don't try it. You should leave that to people who haven't been at a University. They do it so well in the daily papers. What you really are is a Bunburyist. I was quite right in saying you were a Bunburyist. You are one of the most advanced Bunburyists I know. JACK. What on earth do you mean? ALGERNON. You have invented a very useful younger brother called Ernest, in order that you may be able to come up to town as often as you like. I have invented an invaluable permanent invalid called Bunbury, in order that I may be able to go down into the country whenever I choose. Bunbury is perfectly invaluable. If it wasn't for Bunbury's extraordinary bad health, for instance, I wouldn't be able to dine with you at Willis's to-night, for I have been really engaged to Aunt Augusta for more than a week. JACK. I haven't asked you to dine with me anywhere to-night. ALGERNON. I know. You are absurdly careless about sending out invitations. It is very foolish of you. Nothing annoys people so much as not receiving invitations. JACK. You had much better dine with your Aunt Augusta. ALGERNON. I haven't the smallest intention of doing anything of the kind. To begin with, I dined there on Monday, and once a week is quite enough to dine with one's own relations. In the second place, whenever I do dine there I am always treated as a member of the family, and sent down with either no woman at all, or two. In the third place, I know perfectly well whom she will place me next to, to-night. She will place me next Mary Farquhar, who always flirts with her own husband across the dinner-table. That is not very pleasant. Indeed, it is not even decent . . . and that sort of thing is enormously on the increase. The amount of women in London who flirt with their own husbands is perfectly scandalous. It looks so bad. It is simply washing one's clean linen in public. Besides, now that I know you to be a confirmed Bunburyist I naturally want to talk to you about Bunburying. I want to tell you the rules. JACK. I'm not a Bunburyist at all. If Gwendolen accepts me, I am going to kill my brother, indeed I think I'll kill him in any case. Cecily is a little too much interested in him. It is rather a bore. So I am going to get rid of Ernest. And I strongly advise you to do the same with Mr. . . . with your invalid friend who has the absurd name. ALGERNON. Nothing will induce me to part with Bunbury, and if you ever get married, which seems to me extremely problematic, you will be very glad to know Bunbury. A man who marries without knowing Bunbury has a very tedious time of it. JACK. That is nonsense. If I marry a charming girl like Gwendolen, and she is the only girl I ever saw in my life that I would marry, I certainly won't want to know Bunbury. ALGERNON. Then your wife will. You don't seem to realise, that in married life three is company and two is none. JACK. [Sententiously.] That, my dear young friend, is the theory that the corrupt French Drama has been propounding for the last fifty years. ALGERNON. Yes; and that the happy English home has proved in half the time. JACK. For heaven's sake, don't try to be cynical. It's perfectly easy to be cynical. ALGERNON. My dear fellow, it isn't easy to be anything nowadays. There's such a lot of beastly competition about. [The sound of an electric bell is heard.] Ah! that must be Aunt Augusta. Only relatives, or creditors, ever ring in that Wagnerian manner. Now, if I get her out of the way for ten minutes, so that you can have an opportunity for proposing to Gwendolen, may I dine with you to-night at Willis's? JACK. I suppose so, if you want to. ALGERNON. Yes, but you must be serious about it. I hate people

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `STATUS_REVERSAL` (conf: `0.7`)
- **Temporal Horizon:** `LOCAL` | Secondary: `['MISUNDERSTANDING', 'SOCIAL_EMBARRASSMENT']`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "PHYSICAL_COMPLICATION",
  "secondary_mechanisms": [
    "ESCALATION",
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 10,
  "craft_clarity": 10,
  "training_value": 10,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Physical obstacles compound rapidly and the narration remains controlled."
}
```

---

### Passage 078 [PARTIAL] — *Jill The Reckless* (`jill_the_reckless_ch7_07800`)

> "and not quite of the breed we expected," "A gallant young cock enough," the soldier who had whistled answered; He held his lanthorn towards
me and pointed to the white badge on my sleeve.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "PARTIAL",
  "craft_stratum": "REJECT",
  "primary_mechanism": "DIALOGUE_SUBTEXT",
  "secondary_mechanisms": [
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 7,
  "craft_clarity": 5,
  "training_value": 4,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Dialogue has possible subtext but the isolated passage does not establish it strongly enough."
}
```

---

### Passage 079 [PARTIAL] — *Love Among The Chickens* (`love_among_the_chickens_chNone_05495`)

> "  Yanson's small eyes were closing; he seemed to be falling asleep, and he moved so slowly and stiffly that the warden cried to him:  "Hey, there! Quicker! Have you fallen asleep?"  Suddenly Yanson stopped

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [
    "STATUS_REVERSAL",
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Sharp verbal exchange carries the scene, with status and understatement adding secondary effects."
}
```

---

### Passage 080 [PARTIAL] — *My Man Jeeves* (`my_man_jeeves_chNone_00968`)

> Have you ever seen that picture, "The Soul's Awakening"? It represents a flapper of sorts gazing in a startled sort of way into the middle distance with a look in her eyes that seems to say, "Surely that is [COMPANION_B]'s step I hear on the mat! Can this be love?" Well, Bobbie had a soul's awakening too

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "A simple comic problem is extended through successive increasingly absurd consequences."
}
```

---

### Passage 081 [PARTIAL] — *Piccadilly Jim* (`piccadilly_jim_chNone_02909`)

> **Story Outline for Piccadilly Jim**

- **Hook**: A FAIR PENITENT *** Produced by Christopher Hapka A FAIR PENITENT By Wilkie Collins About "A Fair Penitent" This story first appeared in Charles Dickens' magazine, "Household Words," volume 16, number 382, July 18, 1857
- **Midpoint**: knees!" Pious and prophetic man! Before many days had passed his words came true. If he had persiste
- **Climax**: knees!" Pious and prophetic man! Before many days had passed his words came true. If he had persiste

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 5,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Serious dramatic passage; detector appears to be forcing comedy."
}
```

---

### Passage 082 [PARTIAL] — *Psmith In The City* (`psmith_in_the_city_chNone_04412`)

> My Lord, I must confesse, I know this woman, And fiue yeres since there was some speech of marriage Betwixt my selfe, and her: which was broke off,  Partly for that her promis'd proportions Came short of Composition: But in chiefe For that her reputation was dis-valued In leuitie: Since which time of fiue yeres I neuer spake with her, saw her, nor heard from her Vpon my faith, and honor  Mar

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `SOCIAL_EMBARRASSMENT` (conf: `0.25`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "DIALOGUE_SUBTEXT",
  "secondary_mechanisms": [
    "DEADPAN_REACTION",
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Characters communicate more through implication and social restraint than explicit statements."
}
```

---

### Passage 083 [PARTIAL] — *Right Ho* (`right_ho_ch1_06587`)

> "if you want to make a bit of money have something on Wonderchild for the 'Lincolnshire.'," "[COMPANION]," I said, for I'm fond of the man, and like to do him a good turn when I can, He shook his head.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "DRAMATIC_IRONY",
  "secondary_mechanisms": [
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LONG_HORIZON",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "The reader is positioned to understand a discrepancy that the character does not fully perceive."
}
```

---

### Passage 084 [PARTIAL] — *Something Fresh* (`something_fresh_ch6_04748`)

> Speaker: Character | Target Emotion: Urgent / Cautious
"My idea," he said, "was that I should do what I might call the
rough work; and--".

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "PARTIAL",
  "craft_stratum": "REJECT",
  "primary_mechanism": "CALLBACK",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LONG_HORIZON",
  "setup_accurate": true,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 8,
  "craft_clarity": 4,
  "training_value": 4,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Possible callback depends on context outside the excerpt; insufficient local evidence."
}
```

---

### Passage 085 [PARTIAL] — *The Adventures Of Sally* (`the_adventures_of_sally_ch11_06729`)

> "and," The tender brought on board a band of Christian friends, who once
more thronged around her, till the parting signal was given, and then
the last sounds heard on leaving were, "Yes, we part, but not for
ever, Shall we gather at the river?".

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [
    "SOCIAL_EMBARRASSMENT",
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "A mistaken interpretation creates escalating social discomfort and verbal complications."
}
```

---

### Passage 086 [PARTIAL] — *The Diary Of A Nobody* (`the_diary_of_a_nobody_ch1_00212`)

> "Mosaic writer," Gladstone speaks of the author of the first chapter of Genesis as "the Mosaic writer"; I suppose, therefore, that he will admit that it is equally proper to speak of the author of Leviticus as the Whether such a phrase would be used by any one who had an adequate conception of the assured results of modern Biblical criticism is another matter; but, at any rate, it cannot be denied that Leviticus has as much claim to Mosaic authorship as Genesis.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `ESCALATION` (conf: `0.25`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [
    "PHYSICAL_COMPLICATION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Each attempted solution creates a larger problem, producing classic farce escalation."
}
```

---

### Passage 087 [PARTIAL] — *The Inimitable Jeeves* (`the_inimitable_jeeves_ch23_04684`)

> "About the same time, that is to say, Pentecost, 1270," writes
Fitz-Thedmar, "at the instance of Sir Edward, his lordship the king
granted unto the citizens that they might have a mayor from among
themselves in such form as they were wont to elect him.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "PHYSICAL_COMPLICATION",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 4,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Physical action is present, but not as comic physical complication."
}
```

---

### Passage 088 [PARTIAL] — *The Little Nugget* (`the_little_nugget_ch1_06829`)

> "he said," "I take ut the con-sign-y don't want to pay for thim kebbages, If I know signs of refusal, the con-sign-y refuses to pay for wan dang kebbage leaf an' be hanged to me!" Mr.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 8,
  "craft_clarity": 8,
  "training_value": 8,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Compact joke depends on wording, register collision, and dry delivery."
}
```

---

### Passage 089 [PARTIAL] — *The Man Upstairs* (`the_man_upstairs_ch11_01146`)

> "I actually said those identical words! And then I broke down and sobbed. Irene, I BLUBBERED!," "Oh, PLEASE go away, you - you Thug! How dare you think THAT when my leg is asleep? His manner altered in an instant - I could see that much through my fingers and hair.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "SOCIAL_EMBARRASSMENT",
  "secondary_mechanisms": [
    "MISUNDERSTANDING",
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Social embarrassment is intensified by a misunderstanding and restrained reaction."
}
```

---

### Passage 090 [PARTIAL] — *The Prince And Betty* (`the_prince_and_betty_ch1_09711`)

> "Not Death, but Love," Straightway I was 'ware, So weeping, how a mystic Shape did move Behind me, and drew me backward by the hair; And a voice said in mastery, while I strove, - "Guess now who holds thee!" - "Death," I said, But, there, The silver answer rang, But only three in all God's universe Have heard this word thou hast said, - Himself, beside Thee speaking, and me listening! and replied One of us.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "PARTIAL",
  "craft_stratum": "REJECT",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 7,
  "craft_clarity": 4,
  "training_value": 4,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Some sequential intensification, but not enough evidence for a complete comic escalation."
}
```

---

### Passage 091 [PARTIAL] — *Their Mutual Child* (`their_mutual_child_ch12_01161`)

> "willing to acquit," He bluntly told Russell
that while he was Gladstone of "any deliberate
intention to bring on the worst effects," he was bound to say that
Gladstone was doing it quite as certainly as if he had one; and to this
charge, which struck more sharply at Russell's secret policy than at
Gladstone's public defence of it, Russell replied as well as he could:--.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `ESCALATION` (conf: `0.25`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "STATUS_REVERSAL",
  "secondary_mechanisms": [
    "SOCIAL_EMBARRASSMENT",
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Expected hierarchy or confidence is overturned in a socially comic exchange."
}
```

---

### Passage 092 [PARTIAL] — *Three Men In A Boat* (`three_men_in_a_boat_ch13_00559`)

> "Hell Fire Club," The famous Medmenham monks, or as they were
commonly called, and of whom the notorious Wilkes was a member, were
a fraternity whose motto was "Do as you please," and that invitation
still stands over the ruined doorway of the abbey.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `ESCALATION` (conf: `0.25`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [
    "ESCALATION",
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Literal misunderstanding produces a chain of increasingly absurd consequences."
}
```

---

### Passage 093 [PARTIAL] — *Three Men On The Bummel* (`three_men_on_the_bummel_ch7_06810`)

> "That could not have been the case with them all," replied [COMPANION_A], "and
in the course of that journey, I must have fallen against every one of
them at least three times.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 5,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Non-comic exposition/commentary."
}
```

---

### Passage 094 [PARTIAL] — *A Damsel In Distress* (`a_damsel_in_distress_ch32_00194`)

> Chapter VIII:
 "Before his stony eye the immaculate Bartling wilted.
 It was a perfectly astounding likeness, but it was
 apparent to him when what he had ever heard and read
 about doubles came to him." This is a somewhat clumsy construction, and quite un-Wodehousian.
The original passage in the serialization read: "Before his stony eye the immaculate Bartling wilted. All that
 he had ever heard and read about doubles came to him."

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "DEADPAN_REACTION",
  "secondary_mechanisms": [
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "The strongest comic device is an understated response to something objectively absurd."
}
```

---

### Passage 095 [PARTIAL] — *Jill The Reckless* (`jill_the_reckless_ch2_08394`)

> Speaker: Character | Target Emotion: Calm / Conversational
"for my servants is my faith," "The true faith," he answered-- Then a
thought seemed to strike him.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "PHYSICAL_COMPLICATION",
  "secondary_mechanisms": [
    "ESCALATION",
    "MISUNDERSTANDING"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Physical complications and mistaken assumptions interact to create farce."
}
```

---

### Passage 096 [PARTIAL] — *Love Among The Chickens* (`love_among_the_chickens_ch24_04215`)

> "; and he pointed with his finger at the silent gendarme," "What kind of master are
you, if you are going to hang right beside me? There is a master for
you Eh, that
fellow there is not worse than our kind"; he pointed with his eyes at
Vasily.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `ESCALATION` (conf: `0.7`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "PARTIAL",
  "craft_stratum": "REJECT",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 7,
  "craft_clarity": 4,
  "training_value": 4,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Witty fragment without enough setup or payoff."
}
```

---

### Passage 097 [PARTIAL] — *My Man Jeeves* (`my_man_jeeves_ch11_02252`)

> "read old Marshall," "What do you get for slugging a Serene Highness? I wonder if they'll catch the fellow?" "'Later,' 'the pedestrian who discovered His Serene Highness proves to have been Mr.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [
    "DEADPAN_REACTION",
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "A recurring absurdity is escalated while the narrator maintains comic restraint."
}
```

---

### Passage 098 [PARTIAL] — *Piccadilly Jim* (`piccadilly_jim_ch1_05703`)

> "does this man seriously recommend me to lash my own shoulders? Just Heaven, what impertinence! And yet, is it not my duty to put up with it? Does not this apparent insolence proceed from the pen of a holy man? If he tells me to flog my wickedness out of me, is it not my bounden duty to lay on the scourge with all my might immediately? Sinner that I am! I am thinking remorsefully of my plump shoulders and the dimples on my back, when I ought to be thinking of nothing but the cat-o'-nine-tails and obedience to Father Deveaux?," "What!" cried I to myself, These reflections soon gave me the resolution which I had wanted at first.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 6,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Serious scene; no clear comedy craft."
}
```

---

### Passage 099 [PARTIAL] — *Psmith In The City* (`psmith_in_the_city_ch2_05976`)

> Partly for that her promis'd proportions
Came short of Composition: But in chiefe
For that her reputation was dis-valued
In leuitie: Since which time of fiue yeres
I neuer spake with her, saw her, nor heard from her
Vpon my faith, and honor

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `SOCIAL_EMBARRASSMENT` (conf: `0.25`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 8,
  "craft_clarity": 8,
  "training_value": 8,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "A mistaken assumption is unmistakably the engine of the joke."
}
```

---

### Passage 100 [PARTIAL] — *Right Ho* (`right_ho_ch15_03532`)

> "DEAR FREDDIE, - Well, here I am in New York. It's not a bad place. I'm not having a bad time. Everything's pretty all right. The cabarets aren't bad. Don't know when I shall be back. How's everybody? Cheer-o! - Yours," There was I, loving the life, while the mere mention of it gave Rocky a tired feeling; yet here is a letter I wrote to a pal of mine in London: BERTIE.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Comic language and controlled delivery produce the payoff."
}
```

---

### Passage 101 [PARTIAL] — *Something Fresh* (`something_fresh_ch11_07295`)

> CHAPTER XI Blandings Castle dozed in the calm of an English Sunday
afternoon. All was peace. Freddie was in bed, with orders from
the doctor to stay there until further notice. Baxter had washed
his face. Lord Emsworth had returned to his garden fork. The rest
of the house party strolled about the grounds or sat in them, for
the day was one of those late spring days that are warm with a
premature suggestion of midsummer. Aline Peters was sitting at the open window of her bedroom, which
commanded an extensive view of the terraces. A pile of letters
lay on the table beside her, for she had just finished reading
her mail. The postman came late to the castle on Sundays and she
had not been able to do this until luncheon was over. Aline was puzzled. She was conscious of a fit of depression for
which she could in no way account. She had a feeling that all was
not well with the world, which was the more remarkable in that
she was usually keenly susceptible to weather conditions and
reveled in sunshine like a kitten. Yet here was a day nearly as
fine as an American day--and she found no solace in it. She looked down on the terrace; as she looked the figure of
[COMPANION_B] Emerson appeared, walking swiftly. And at the sight of him
something seemed to tell her that she had found the key to her
gloom. There are many kinds of walk. [COMPANION_B] Emerson's was the walk of
mental unrest. His hands were clasped behind his back, his eyes
stared straight in front of him from beneath lowering brows, and
between his teeth was an unlighted cigar. No man who is not a
professional politician holds an unlighted cigar in his mouth
unless he wishes to irritate and baffle a ticket chopper in the
subway, or because unpleasant meditations have caused him to
forget he has it there. Plainly, then, all was not well with
[COMPANION_B] Emerson. Aline had suspected as much at luncheon; and looking back she
realized that it was at luncheon her depression had begun. The
discovery startled her a little. She had not been aware, or she
had refused to admit to herself, that [COMPANION_B]'s troubles bulked so
large on her horizon. She had always told herself that she liked
[COMPANION_B], that [COMPANION_B] was a dear old friend, that [COMPANION_B] amused and
stimulated her; but she would have denied she was so wrapped up
in [COMPANION_B] that the sight of him in trouble would be enough to
spoil for her the finest day she had seen since she left America. There was something not only startling but shocking in the
thought; for she was honest enough with herself to recognize that
Freddie, her official loved one, might have paced the grounds of
the castle chewing an unlighted cigar by the hour without
stirring any emotion in her at all. And she was to marry Freddie next month! This was surely a matter
that called for thought. She proceeded, gazing down the while at
the perambulating [COMPANION_B], to give it thought. Aline's was not a deep nature. She had never pretended to herself
that she loved the Honorable Freddie in the sense in which the
word is used in books. She liked him and she liked the idea of
being connected with the peerage; her father liked the idea and
she liked her father. And the combination of these likings had
caused her to reply "Yes" when, last Autumn, Freddie, swelling
himself out like an embarrassed frog and gulping, had uttered
that memorable speech beginning, "I say, you know, it's like
this, don't you know!"--and ending, "What I mean is, will you
marry me--what?" She had looked forward to being placidly happy as the Honorable
Mrs. Frederick Threepwood. And then [COMPANION_B] Emerson had reappeared
in her life, a disturbing element. Until to-day she would have resented the suggestion that she was
in love with [COMPANION_B]. She liked to be with him, partly because he
was so easy to talk to, and partly because it was exciting to be
continually resisting the will power he made no secret of trying
to exercise. But to-day there was a difference. She had suspected
it at luncheon and she realized it now. As she looked down at him
from behind the curtain, and marked his air of gloom, she could
no longer disguise it from herself. She felt maternal--horribly maternal. [COMPANION_B] was in trouble and
she wanted to comfort him. Freddie, too, was in trouble. But did she want to comfort
Freddie? No. On the contrary, she was already regretting her
promise, so lightly given before luncheon, to go and sit with him
that afternoon. A well-marked feeling of annoyance that he should
have been so silly as to tumble downstairs and sprain his ankle
was her chief sentiment respecting Freddie. [COMPANION_B] Emerson continued to perambulate and Aline continued to
watch him. At last she could endure it no longer. She gathered up
her letters, stacked them in a corner of the dressing-table and
left the room. [COMPANION_B] had reached the end of the terrace and
turned when she began to descend the stone steps outside the
front door. He quickened his pace as he caught sight of her. He
halted before her and surveyed her morosely. "I have been looking for you," he said. "And here I am. Cheer up, [COMPANION_B]! Whatever is the matter? I've
been sitting in my room looking at you, and you have been simply
prowling. What has gone wrong?" "Everything!" "How do you mean--everything?" "Exactly what I say. I'm done for. Read this." Aline took the yellow slip of paper. "A cable," added [COMPANION_B]. "I
got it this morning--mailed on from my rooms in London. Read it." "I'm trying to. It doesn't seem to make sense." [COMPANION_B] laughed grimly. "It makes sense all right." "I don't see how you can say that. 'Meredith elephant
kangaroo--?'" "Office cipher; I was forgetting. 'Elephant' means 'Seriously ill
and unable to attend to duty.' Meredith is one of the partners in
my firm in New York." "Oh, I'm so sorry! Do you think he is very sick? Are you very
fond of Mr. Meredith?" "Meredith is a good fellow and I like him; but if it was simply a
matter of his being ill I'm afraid I could manage to bear up
under the news. Unfortunately 'kangaroo' means 'Return, without
fail, by the next boat.'" "You must return by the next boat?" Aline looked at him, in her
eyes a slow-growing comprehension of the situation. "Oh!" she
said at length. "I put it stronger than that," said [COMPANION_B]. "But--the next boat---- That means on Wednesday." "Wednesday morning, from Southampton. I shall have to leave here
to-morrow." Aline's eyes were fixed on the blue hills across the valley, but
she did not see them. There was a mist between. She was feeling
crushed and ill-treated and lonely. It was as though [COMPANION_B] was
already gone and she left alone in an alien land. "But, [COMPANION_B]!" she said; she could find no other words for her
protest against the inevitable. "It's bad luck," said Emerson quietly; "but I shouldn't wonder if
it is not the best thing that really could have happened. It
finishes me cleanly, instead of letting me drag on and make both
of us miserable. If this cable hadn't come I suppose I should
have gone on bothering you up to the day of your wedding. I
should have fancied, to the last moment, that there was a chance
for me; but this ends me with one punch. "Even I haven't the nerve to imagine that I can work a miracle in
the few hours before the train leaves to-morrow. I must just make
the best of it. If we ever meet again--and I don't see why we
should--you will be married. My particular brand of mental
suggestion doesn't work at long range. I shan't hope to influence
you by telepathy." He leaned on the balustrade at her side and spoke in a low, level
voice. "This thing," he said, "coming as a shock, coming out of the blue
sky without warning--Meredith is the last man in the world you
would expect to crack up; he looked as fit as a dray horse the
last time I saw him--somehow seems to have hammered a certain
amount of sense into me. Odd it never struck me before; but I
suppose I have been about the most bumptious, conceited fool that
ever happened. "Why I should have imagined that there was a sort of irresistible
fascination in me, which was bound to make you break off your
engagement and upset the whole universe simply to win the
wonderful reward of marrying me, is more than I can understand. I
suppose it takes a shock to make a fellow see exactly what he
really amounts to. I couldn't think any more of you than I do;
but, if I could, the way you have put up with my mouthing and
swaggering and posing as a sort of superman, would make me do it.
You have been wonderful!" Aline could not speak. She felt as though her whole world had
been turned upside down in the last quarter of an hour. This was
a new [COMPANION_B] Emerson, a [COMPANION_B] at whom it was impossible to
laugh, but an insidiously attractive [COMPANION_B]. Her heart beat
quickly. Her mind was not clear; but dimly she realized that he
had pulled down her chief barrier of defense and that she was
more open to attack than she had ever been. Obstinacy, the
automatic desire to resist the pressure of a will that attempted
to overcome her own, had kept her cool and level-headed in the
past. With masterfulness she had been able to cope. Humility was
another thing altogether. Soft-heartedness was Aline's weakness. She had never clearly
recognized it, but it had been partly pity that had induced her
to accept Freddie; he had seemed so downtrodden and sorry for
himself during those Autumn days when they had first met.
Prudence warned her that strange things might happen if once she
allowed herself to pity [COMPANION_B] Emerson. The silence lengthened. Aline could find nothing to say. In her
present mood there was danger in speech. "We have known each other so long," said Emerson, "and I have
told you so often that I love you, we have come to make almost a
joke of it, as though we were playing some game. It just happens
that that is our way--to laugh at things; but I am going to say
it once again, even though it has come to be a sort of catch
phrase. I love you! I'm reconciled to the fact that I am done
for, out of the running, and that you are going to marry somebody
else; but I am not going to stop loving you. "It isn't a question of whether I should be happier if I forgot
you. I can't do it. It's just an impossibility--and that's all
there is to it. Whatever I may be to you, you are part of me, and
you always will be part of me. I might just as well try to go on
living without breathing as living without loving you." He stopped and straightened himself. "That's all! I don't want to spoil a perfectly good Spring
afternoon for you by pulling out the tragic stop. I had to say
all that; but it's the last time. It shan't occur again. There
will be no tragedy when I step into the train to-morrow. Is there
any chance that you might come and see me off?" Aline nodded. "You will? That will be splendid! Now I'll go and pack and break
it to my host that I must leave him. I expect, it will be news to
him to learn that I am here. I doubt if he knows me by sight." Aline stood where he had left her, leaning on the balustrade. In
the fullness of time there came to her the recollection she had
promised Freddie that shortly after luncheon she would sit with
him.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `ESCALATION` (conf: `0.7`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "PARTIAL",
  "craft_stratum": "REJECT",
  "primary_mechanism": "SOCIAL_EMBARRASSMENT",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 7,
  "craft_clarity": 4,
  "training_value": 4,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Embarrassment is suggested but not sufficiently developed in the excerpt."
}
```

---

### Passage 102 [PARTIAL] — *The Adventures Of Sally* (`the_adventures_of_sally_ch10_00048`)

> "What I do, thou knowest not now, but thou shalt know hereafter," Blessed hereafter! when we shall see _all_ the way the Lord our
God has led us; not a smooth way, not an easy way.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [
    "MISUNDERSTANDING",
    "PHYSICAL_COMPLICATION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Attempts to fix the problem repeatedly make it worse."
}
```

---

### Passage 103 [PARTIAL] — *The Diary Of A Nobody* (`the_diary_of_a_nobody_ch2_04365`)

> "Evolution," Gladstone in matters which lie as much within the province of Literature and History as in that of Science; but if any one desirous of further knowledge will be so good as to turn to that most excellent and by no means recondite source of information, the "Encyclopaedia Britannica," he will find, under the letter E, the word and a long article on that subject.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "STATUS_REVERSAL",
  "secondary_mechanisms": [
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "A social expectation is cleanly overturned, making this useful as a status example."
}
```

---

### Passage 104 [PARTIAL] — *The Inimitable Jeeves* (`the_inimitable_jeeves_ch37_00036`)

> "his diets," An additional
reason for the delay in carrying out Gresham's project may perhaps be
found in the fact that, during his absence on the queen's business in
1563, Elizabeth had, with her usual parsimony, cut down Gresham's
allowance of twenty shillings a day for Gresham complained
bitterly of this abridgment of his income in a letter to Secretary Cecil,
and also in another letter couched in more guarded terms to the queen
herself.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "DRAMATIC_IRONY",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LONG_HORIZON",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 6,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "The apparent irony is historical/narrative rather than a comic dramatic-irony mechanism."
}
```

---

### Passage 105 [PARTIAL] — *The Little Nugget* (`the_little_nugget_ch1_05265`)

> "Here's the rule for ut. 'Whin the agint be in anny doubt regardin' which of two rates applies to a shipment, he shall charge the larger. The con-sign-ey may file a claim for the overcharge.' In this case, Misther Morehouse, I be in doubt. Pets thim animals may be, an' domestic they be, but pigs I'm blame sure they do be, an' me rules says plain as the nose on yer face, 'Pigs Franklin to Westcote, thirty cints each.' An' Mister Morehouse, by me arithmetical knowledge two times thurty comes to sixty cints," Mr.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `ESCALATION` (conf: `0.25`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "DIALOGUE_SUBTEXT",
  "secondary_mechanisms": [
    "DEADPAN_REACTION",
    "SOCIAL_EMBARRASSMENT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Characters avoid saying the obvious thing, and the gap creates comic tension."
}
```

---

### Passage 106 [PARTIAL] — *The Man Upstairs* (`the_man_upstairs_ch6_08632`)

> "Rebecca hesitated. Her face was very pale. She looked with an appeal that was fairly agonizing at her sister Caroline," Why don't you set the lamp on the study table in the middle of the room, then we can both see? Why don't you put the lamp on this table, as she says?" asked Caroline, almost fiercely.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [
    "VERBAL_WIT",
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 10,
  "craft_clarity": 10,
  "training_value": 10,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Strong multi-stage escalation with increasingly absurd consequences."
}
```

---

### Passage 107 [PARTIAL] — *The Prince And Betty* (`the_prince_and_betty_ch1_02331`)

> "I love her for her smile - her look - her way Of speaking gently, - for a trick of thought That falls in well with mine, and certes brought A sense of pleasant ease on such a day," Do not say For these things in themselves, Belovëd, may Be changed, or change for thee, - and love, so wrought, May be unwrought so.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "PARTIAL",
  "craft_stratum": "REJECT",
  "primary_mechanism": "CALLBACK",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LONG_HORIZON",
  "setup_accurate": true,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 7,
  "craft_clarity": 4,
  "training_value": 4,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Potential callback cannot be confirmed without longer-horizon context."
}
```

---

### Passage 108 [PARTIAL] — *Their Mutual Child* (`their_mutual_child_ch13_04651`)

> "Life of Gladstone," He no longer cared whether he
understood human nature or not; he understood quite as much of it as he
wanted; but he found in the (II, 464) a remark
several times repeated that gave him matter for curious thought.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [
    "MISUNDERSTANDING"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 8,
  "craft_clarity": 8,
  "training_value": 8,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "The comic effect rests on a semantic/literal interpretation."
}
```

---

### Passage 109 [PARTIAL] — *Three Men In A Boat* (`three_men_in_a_boat_ch6_03811`)

> "[COMPANION_A] had a glass of bitter in this house;," I wonder now, supposing [COMPANION_A], say, turned over a new
leaf, and became a great and good man, and got to be Prime Minister,
and died, if they would put up signs over the public-houses that he had
patronised: "[COMPANION_A] had
two of Scotch cold here in the summer of '88;" "[COMPANION_A] was chucked from
here in December, 1886.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "SOCIAL_EMBARRASSMENT",
  "secondary_mechanisms": [
    "ESCALATION",
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Embarrassment intensifies through successive social complications."
}
```

---

### Passage 110 [PARTIAL] — *Three Men On The Bummel* (`three_men_on_the_bummel_ch2_01179`)

> Speaker: Ethelbertha | Target Emotion: Urgent / Cautious
"I should not grumble at them," said Ethelbertha; "we might get some of
the other sort, and like them still less.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "PHYSICAL_COMPLICATION",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 4,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Physical event is serious rather than comic."
}
```

---

### Passage 111 [PARTIAL] — *A Damsel In Distress* (`a_damsel_in_distress_ch32_10335`)

> Chapter VIII:
 "Before his stony eye the immaculate Bartling wilted.
 It was a perfectly astounding likeness, but it was
 apparent to him when what he had ever heard and read
 about doubles came to him."

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [
    "DEADPAN_REACTION",
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "A misunderstanding is sustained by characters treating the premise seriously."
}
```

---

### Passage 112 [PARTIAL] — *Jill The Reckless* (`jill_the_reckless_ch5_02843`)

> "your sister must leave with us at once.  We have no time to lose," "Come," the priest
continued peremptorily, turning to the lady who had entered with him,.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Classic escalating absurdity with a clear terminal payoff."
}
```

---

### Passage 113 [PARTIAL] — *Love Among The Chickens* (`love_among_the_chickens_ch13_10152`)

> Speaker: English | Target Emotion: Calm / Conversational
"The Story of the Seven Who Were Hanged," I am very glad that will be
read in English.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "PARTIAL",
  "craft_stratum": "REJECT",
  "primary_mechanism": "DIALOGUE_SUBTEXT",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 7,
  "craft_clarity": 4,
  "training_value": 4,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Subtext may be present but is not sufficiently clear in isolation."
}
```

---

### Passage 114 [PARTIAL] — *My Man Jeeves* (`my_man_jeeves_ch9_02910`)

> "Why, they change the programme every week there," How does that hit you?" "It's a fine bit of memorizing," I said; "but how does it help?" "Ah!" I said.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "STATUS_REVERSAL",
  "secondary_mechanisms": [
    "DEADPAN_REACTION",
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 10,
  "craft_clarity": 10,
  "training_value": 10,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Excellent reversal of expected social competence/status, followed by a restrained punchline."
}
```

---

### Passage 115 [PARTIAL] — *Piccadilly Jim* (`piccadilly_jim_ch1_02278`)

> "You forget that this is her farewell dinner to her friends!," Just Heaven! what did I not suffer some days afterwards, when I united around me at dinner, for the last time, all the friends who had been dearest to me in the days of my worldly life! What words can describe the tumult of my heart when one of my guests said to me, "You are giving us too good a dinner for a Wednesday in Passion Week;" and when another answered, jestingly, I felt ready to faint while they were talking, and rose from table pretexting as an excuse, that I had a payment to make that evening, which I could not in honour defer any longer.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 5,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "No self-contained comic engine."
}
```

---

### Passage 116 [PARTIAL] — *Psmith In The City* (`psmith_in_the_city_ch2_00921`)

> Partly for that her promis'd proportions
Came short of Composition: But in chiefe
For that her reputation was dis-valued
In leuitie: Since which time of fiue yeres
I neuer spake with her, saw her, nor heard from her
Vpon my faith, and honor

Mar. Noble Prince,
As there comes light from heauen, and words fro[m] breath,
As there is sence in truth, and truth in vertue,
I am affianced this mans wife, as strongly
As words could make vp vowes: And my good Lord,
But Tuesday night last gon, in's garden house,
He knew me as a wife. As this is true,
Let me in safety raise me from my knees,
Or else for euer be confixed here
A Marble Monument

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `SOCIAL_EMBARRASSMENT` (conf: `0.25`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "PHYSICAL_COMPLICATION",
  "secondary_mechanisms": [
    "ESCALATION",
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Physical mishaps are deliberately compounded and verbally framed for comic effect."
}
```

---

### Passage 117 [PARTIAL] — *Right Ho* (`right_ho_ch13_03473`)

> "did you meet a mewing cat outside? I feel positive I heard a cat mewing," "Father," said Clarence, "No," said the father, shaking his head; "no mewing cat.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "PARTIAL",
  "craft_stratum": "REJECT",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 7,
  "craft_clarity": 4,
  "training_value": 4,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Some comic phrasing, but not enough structural evidence."
}
```

---

### Passage 118 [PARTIAL] — *Something Fresh* (`something_fresh_ch9_03293`)

> "Are you satisfied now, my dear Baxter," said the earl, "or is
there any more furniture that you would like to break? You know,
this furniture breaking is becoming a positive craze with you, my
dear fellow.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "DEADPAN_REACTION",
  "secondary_mechanisms": [
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Strong understatement makes an absurd event funnier."
}
```

---

### Passage 119 [PARTIAL] — *The Adventures Of Sally* (`the_adventures_of_sally_ch14_04050`)

> "Bright Jewels," To hear
that dear little fellow sing and look around over
the group of little ones, far from native home, and father and
mother, brother and sister, and think, "These are the jewels,
precious jewels," it seemed to bring heaven near.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [
    "MISUNDERSTANDING",
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Misunderstanding is repeatedly intensified while the narration remains controlled."
}
```

---

### Passage 120 [PARTIAL] — *The Diary Of A Nobody* (`the_diary_of_a_nobody_ch2_03475`)

> "In the later system of emanation of Sankhya there is a more marked approach to a materialistic doctrine of evolution," " And again: What little knowledge I have of the matter--chiefly derived from that very instructive book, "Die Religion des Buddha," by C.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 5,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Expository or serious material without comic craft."
}
```

---

### Passage 121 [PARTIAL] — *The Inimitable Jeeves* (`the_inimitable_jeeves_ch28_06639`)

> "Grenecobbe," (638) In a list, containing nearly 200 names of divers persons of
bad character, who had left the city by reason of the insurrection,(639)
there appear the names of two servants of Henry The name is
far from common, and we shall not perhaps be far wrong in conjecturing
that the owner of it was a relation of William "Gryndecobbe," who led the
insurgents against the abbey of St.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Literal misunderstanding creates the central comic situation."
}
```

---

### Passage 122 [PARTIAL] — *The Little Nugget* (`the_little_nugget_ch1_08466`)

> "Dr. Sir--We are in receipt of your letter regarding rate on guinea-pigs between Franklin and Westcote addressed to the president of this company. All claims for overcharge should be addressed to the Claims Department," "Subject--Rate on guinea-pigs," it said, Mr.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `ESCALATION` (conf: `0.95`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [
    "DEADPAN_REACTION",
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Repeated consequences intensify an already absurd premise."
}
```

---

### Passage 123 [PARTIAL] — *The Man Upstairs* (`the_man_upstairs_ch36_06756`)

> "Let nothing irritate you. I will leave a composing draught with your daughter, which she will give you immediately. I will see you in the morning. You will be well in a week," "Thank God!" came in a murmur from a dusk corner near the door.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "PARTIAL",
  "craft_stratum": "REJECT",
  "primary_mechanism": "DIALOGUE_SUBTEXT",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 7,
  "craft_clarity": 4,
  "training_value": 4,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Possible subtext, but the fragment does not provide enough evidence."
}
```

---

### Passage 124 [PARTIAL] — *Their Mutual Child* (`their_mutual_child_ch13_00105`)

> "incredible grossness," Of the obstinate effort to bring about an armed intervention,
on the lines marked out by Russell's letter to Palmerston from Gotha,
17 September, 1862, nothing could be said beyond Gladstone's plea in
excuse for his speech in pursuance of the same effort, that it was "the
most singular and palpable error," "the least excusable," "a mistake of
incredible grossness," which passed defence; but while Gladstone threw
himself on the mercy of the public for his speech, he attempted no
excuse for Lord Russell who led him into the of
announcing the Foreign Secretary's intent.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.25`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 5,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Serious/expository material rather than comedy."
}
```

---

### Passage 125 [PARTIAL] — *Three Men In A Boat* (`three_men_in_a_boat_ch9_05437`)

> Speaker: Emily | Target Emotion: Calm / Conversational
"Go back, Emily, and see what it is they want," says one; and Emily
comes back, and asks what it is.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "The line-level wording and ironic register carry the joke."
}
```

---

### Passage 126 [PARTIAL] — *Three Men On The Bummel* (`three_men_on_the_bummel_ch1_06419`)

> "If, in the course of fourteen days," I said, "they eat half of what is
on this yacht, they will want a fairly long time for every meal.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "SOCIAL_EMBARRASSMENT",
  "secondary_mechanisms": [
    "STATUS_REVERSAL",
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "A socially awkward encounter develops through status and verbal pressure."
}
```

---

### Passage 127 [PARTIAL] — *A Damsel In Distress* (`a_damsel_in_distress_ch26_04466`)

> Speaker: Character | Target Emotion: Calm / Conversational
"Wait a mom'nt," replied that clear-headed maiden, picking her
teeth thoughtfully with the muzzle of her revolver.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "PHYSICAL_COMPLICATION",
  "secondary_mechanisms": [
    "ESCALATION",
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 10,
  "craft_clarity": 10,
  "training_value": 10,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Physical farce is unmistakable and layered with restrained narration."
}
```

---

### Passage 128 [PARTIAL] — *Jill The Reckless* (`jill_the_reckless_ch4_08793`)

> Speaker: Character | Target Emotion: Fearful
"Now perhaps you will listen to me," he went on smoothly, "and hear
what I am going to do.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "PARTIAL",
  "craft_stratum": "REJECT",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 6,
  "craft_clarity": 4,
  "training_value": 3,
  "keep_verdict": "REJECT",
  "detector_correct": true,
  "notes": "Comic premise is plausible but too fragmentary."
}
```

---

### Passage 129 [PARTIAL] — *Love Among The Chickens* (`love_among_the_chickens_ch17_06637`)

> "Well, what a fool! Of course it can be done with music. This way!," and
he began to sing, with a bold and daring swing.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "DEADPAN_REACTION",
  "secondary_mechanisms": [
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "The character's underreaction to an absurd event is the cleanest mechanism."
}
```

---

### Passage 130 [PARTIAL] — *My Man Jeeves* (`my_man_jeeves_ch3_06274`)

> "No, no! Darling Motty is essentially a home bird. Aren't you, Motty darling?," "Put him up? For my clubs?" Motty, who was sucking the knob of his stick, uncorked himself.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "STATUS_REVERSAL",
  "secondary_mechanisms": [
    "VERBAL_WIT",
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Hierarchy is inverted through a dry verbal exchange."
}
```

---

### Passage 131 [PARTIAL] — *Piccadilly Jim* (`piccadilly_jim_ch1_04906`)

> "Do you come to reward God for making you the attractive person that you are, by mortally transgressing His laws every day of your life?," I hear that question, and I am unspeakably overwhelmed by it.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 5,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Narrative progression without comic escalation."
}
```

---

### Passage 132 [PARTIAL] — *Right Ho* (`right_ho_ch16_01528`)

> "[COMPANION] projected himself into the room with the tea. I was jolly glad to see him. There's nothing like having a bit of business arranged for one when one isn't certain of one's lines. With the teapot to fool about with I felt happier," What I mean is - - Tea, tea, tea - what? What?" I said.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [
    "ESCALATION",
    "SOCIAL_EMBARRASSMENT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Mistaken assumptions create both escalating complications and social discomfort."
}
```

---

### Passage 133 [PARTIAL] — *Something Fresh* (`something_fresh_ch5_02847`)

> Speaker: Miss | Target Emotion: Calm / Conversational
"Mr. Judson is clever, isn't he, Mr. Marson?," whispered Miss
Willoughby, gazing with adoring eyes at the speaker.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 10,
  "craft_clarity": 10,
  "training_value": 10,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Excellent staged escalation with a clear comic payoff."
}
```

---

### Passage 134 [PARTIAL] — *The Adventures Of Sally* (`the_adventures_of_sally_ch18_01608`)

> Speaker: Rescued | Target Emotion: Calm / Conversational
"saved from drink," "Rescued from a workhouse life"
might be written on many a bright little brow, and on many more.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "PARTIAL",
  "craft_stratum": "REJECT",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 7,
  "craft_clarity": 4,
  "training_value": 4,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Incidental wit is present, but the passage is not a robust craft demonstration."
}
```

---

### Passage 135 [PARTIAL] — *The Diary Of A Nobody* (`the_diary_of_a_nobody_ch3_06742`)

> "In the day that Elohim created man, in the likeness of Elohim made he him; male and female created he them; and blessed them and called their name Adam in the day when they were created. And Adam lived an hundred and thirty years and begat _a son_ in his own likeness, after his image; and called his name Seth," I find it impossible to read this passage without being convinced that, when the writer says Adam was made in the likeness of Elohim, he means the same sort of likeness as when he says that Seth was begotten in the likeness of Adam.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "DIALOGUE_SUBTEXT",
  "secondary_mechanisms": [
    "DEADPAN_REACTION",
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Meaning is carried by implication, avoidance, and social restraint."
}
```

---

### Passage 136 [PARTIAL] — *The Inimitable Jeeves* (`the_inimitable_jeeves_ch24_03743`)

> "to which the earl replied, with equal determination," "By God, earl," cried the
king, fairly roused by the obstinacy of his vassal, "you shall either go
or hang; By the
same token, O king, I will neither go nor hang.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "SOCIAL_EMBARRASSMENT",
  "secondary_mechanisms": [
    "MISUNDERSTANDING",
    "ESCALATION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Public/social discomfort compounds through misunderstanding."
}
```

---

### Passage 137 [PARTIAL] — *The Little Nugget* (`the_little_nugget_ch1_02938`)

> "Your letter of the 16th inst., addressed to this Department, subject rate on guinea-pigs from Franklin to Westcote, ree'd. We have taken up the matter with our agent at Westcote, and his reply is attached herewith. He informs us that you refused to receive the consignment or to pay the charges. You have therefore no claim against this company, and your letter regarding the proper rate on the consignment should be addressed to our Tariff Department," Mr.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `ESCALATION` (conf: `0.85`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "PHYSICAL_COMPLICATION",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 4,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Physical action is serious rather than comic."
}
```

---

### Passage 138 [PARTIAL] — *The Man Upstairs* (`the_man_upstairs_ch36_03632`)

> "go to him. See if he is dead - I dare not look," "He is there," said the girl; I made my way as well as I could through the numberless dilapidated chemical instruments with which the room was littered.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Strong conversational wit delivered with dry restraint."
}
```

---

### Passage 139 [PARTIAL] — *Their Mutual Child* (`their_mutual_child_ch23_03975`)

> "Appleton's Cyclopedia," John Fiske went so far in his notice of
the family in as to say that Henry had left a
great reputation at Harvard College; which was a proof of John Fiske's
personal regard that Adams heartily returned; and set the kind
expression down to camaraderie.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `SOCIAL_EMBARRASSMENT` (conf: `0.25`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [
    "MISUNDERSTANDING",
    "PHYSICAL_COMPLICATION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 10,
  "craft_clarity": 10,
  "training_value": 10,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Classic farce structure: each attempted solution creates another complication."
}
```

---

### Passage 140 [PARTIAL] — *Three Men In A Boat* (`three_men_in_a_boat_ch6_02985`)

> "Presents from Ramsgate," The
blue-and-white mugs of the present-day roadside inn will be hunted up,
all cracked and chipped, and sold for their weight in gold, and rich
people will use them for claret cups; and travellers from Japan will
buy up all the and "Souvenirs of Margate,"
that may have escaped destruction, and take them back to Jedo as
ancient English curios.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "PARTIAL",
  "craft_stratum": "REJECT",
  "primary_mechanism": "CALLBACK",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LONG_HORIZON",
  "setup_accurate": true,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 7,
  "craft_clarity": 4,
  "training_value": 3,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Possible long-horizon callback cannot be validated from the excerpt."
}
```

---

### Passage 141 [PARTIAL] — *Three Men On The Bummel* (`three_men_on_the_bummel_ch9_07654`)

> "alone ladies," There are special paths for "wheel-riders"
and special paths for "foot-goers," avenues for "horse-riders," roads for
people in light vehicles, and roads for people in heavy vehicles; ways
for children and for That no particular route has yet
been set aside for bald-headed men or "new women" has always struck me as
an omission.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 8,
  "craft_clarity": 8,
  "training_value": 8,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "A semantic misunderstanding is clean and transferable."
}
```

---

### Passage 142 [PARTIAL] — *A Damsel In Distress* (`a_damsel_in_distress_ch24_02091`)

> "The only trouble is, Jim," he said, peering at himself in the
glass, "shan't I scare the boy to death directly he sees me?
Oughtn't I to give him some sort of warning?".

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 5,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "No sufficiently clear comic engine."
}
```

---

### Passage 143 [PARTIAL] — *Jill The Reckless* (`jill_the_reckless_ch11_04958`)

> "he ejaculated with emotion," "It
was like you! It was like her cousins!
Brave, brave lads!  The Vicomte will live to be proud of you!  Some day
you will all do great things!  I say it!".

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "DEADPAN_REACTION",
  "secondary_mechanisms": [
    "ESCALATION",
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 10,
  "craft_clarity": 10,
  "training_value": 10,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Excellent deadpan handling of an increasingly absurd circumstance."
}
```

---

### Passage 144 [PARTIAL] — *Love Among The Chickens* (`love_among_the_chickens_ch24_06790`)

> "Yes," answered Werner, almost laughing with unexpected jollity, and he
waved his hand easily and freely, as though he were speaking of some
absurd and trifling joke which kind but terribly comical people wanted
to play on him.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "STATUS_REVERSAL",
  "secondary_mechanisms": [
    "SOCIAL_EMBARRASSMENT",
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Social hierarchy and confidence are overturned for comic effect."
}
```

---

### Passage 145 [PARTIAL] — *My Man Jeeves* (`my_man_jeeves_ch14_02699`)

> "He grabbed again, at me this time, and got me by the arm. He had a grip like a lobster," Young man," he said, "you would not betray me? You would not tell Clarence?" I was feeling most frightfully sorry for the poor old chap by this time, don't you know, but I thought it would be kindest to give it him straight instead of breaking it by degrees.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "PARTIAL",
  "craft_stratum": "REJECT",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 7,
  "craft_clarity": 4,
  "training_value": 4,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Some intensification but insufficient comic structure."
}
```

---

### Passage 146 [PARTIAL] — *Piccadilly Jim* (`piccadilly_jim_ch2_00318`)

> "Pious and prophetic man! Before many days had passed his words came true. If he had persisted severely in ordering me to flog myself, I might have opposed him for months together; but, as it was, who could resist the amiable indulgence he showed towards my weakness? The very next day after my interview, I began to feel ashamed of my own cowardice; and the day after that I went down on my knees, exactly as he had predicted, and said," knees! Father Deveaux, give me back my cat-o'-nine-tails.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `SOCIAL_EMBARRASSMENT` (conf: `0.25`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "PHYSICAL_COMPLICATION",
  "secondary_mechanisms": [
    "ESCALATION",
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Physical complication is clearly comic and progressively worsens."
}
```

---

### Passage 147 [PARTIAL] — *Right Ho* (`right_ho_ch15_07797`)

> "The crux of the matter would appear to be, sir, that Mr. Todd is obliged by the conditions under which the money is delivered into his possession to write Miss [FRIEND] long and detailed letters relating to his movements, and the only method by which this can be accomplished, if Mr. Todd adheres to his expressed intention of remaining in the country, is for Mr. Todd to induce some second party to gather the actual experiences which Miss [FRIEND] wishes reported to her, and to convey these to him in the shape of a careful report, on which it would be possible for him, with the aid of his imagination, to base the suggested correspondence," Having got which off the old diaphragm, [COMPANION] was silent.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 6,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Serious or informational material."
}
```

---

### Passage 148 [PARTIAL] — *Something Fresh* (`something_fresh_ch11_06208`)

> "--and ending," And the combination of these likings had
caused her to reply "Yes" when, last Autumn, Freddie, swelling
himself out like an embarrassed frog and gulping, had uttered
that memorable speech beginning, "I say, you know, it's like
this, don't you know! What I mean is, will you
marry me--what?".

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Compact verbal joke with controlled delivery."
}
```

---

### Passage 149 [PARTIAL] — *The Adventures Of Sally* (`the_adventures_of_sally_ch17_04053`)

> "Strength is small;," "Without me ye can do nothing;" "Is there not an
appointed warfare (margin) to man upon earth?" He, who has appointed
the warfare will not send any at their own charges.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [
    "SOCIAL_EMBARRASSMENT",
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Misunderstanding drives an increasingly awkward social exchange."
}
```

---

### Passage 150 [PARTIAL] — *The Diary Of A Nobody* (`the_diary_of_a_nobody_ch4_01256`)

> "that is pleasant to the sight and good for food," The creation of living beings begins with that of a solitary man; the next thing that happens is the laying out of the Garden of Eden, and the causing the growth from its soil of every tree ; the third act is the formation out of the ground of "every beast of the field, and every fowl of the air"; the fourth and last, the manufacture of the first woman from a rib, extracted from Adam, while in a state of anaesthesia.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [
    "VERBAL_WIT",
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "A comic premise expands through increasingly extreme examples."
}
```

---

### Passage 151 [PARTIAL] — *The Inimitable Jeeves* (`the_inimitable_jeeves_ch25_00309`)

> "Muns," " They were the
precursors of the the "Tityre Tus," the "Hectors," and the
"Scourers,"--dynasties of tyrants, as Macaulay styles them, which
domineered over the streets of London, soon after the Restoration, and at
a later period were superseded by the "Nickers," the "Hawcubites," and the
still more dreaded "Mohawks," of Queen Anne's reign.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `SOCIAL_EMBARRASSMENT` (conf: `0.25`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "DRAMATIC_IRONY",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LONG_HORIZON",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 5,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Irony is not functioning as a transferable comic dramatic-irony mechanism."
}
```

---

### Passage 152 [PARTIAL] — *The Little Nugget* (`the_little_nugget_ch1_08298`)

> "Probably starved to death by this time! Add this to that letter: 'Give condition of consignment at present.'," He tossed the papers on to the stenographer's desk, took his feet from his own desk and went out to lunch.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "SOCIAL_EMBARRASSMENT",
  "secondary_mechanisms": [
    "STATUS_REVERSAL",
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Public embarrassment is created by a reversal in expected social control."
}
```

---

### Passage 153 [PARTIAL] — *The Man Upstairs* (`the_man_upstairs_ch40_08306`)

> Speaker: Elizabeth | Target Emotion: Fearful
"But what if the world will not believe that it is the type of an innocent sorrow?," " urged Elizabeth.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "PARTIAL",
  "craft_stratum": "REJECT",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 7,
  "craft_clarity": 4,
  "training_value": 4,
  "keep_verdict": "REJECT",
  "detector_correct": true,
  "notes": "Possible misunderstanding but insufficient setup/payoff."
}
```

---

### Passage 154 [PARTIAL] — *Their Mutual Child* (`their_mutual_child_ch19_08933`)

> "The best way to treat a bad law is to execute it," Simple-minded beyond the experience of Wall Street or State Street, he
resorted, like most men of the same intellectual calibre, to
commonplaces when at a loss for expression: "Let us have peace!" or, ; or a score of such
reversible sentences generally to be gauged by their sententiousness;
but sometimes he made one doubt his good faith; as when he seriously
remarked to a particularly bright young woman that Venice would be a
fine city if it were drained.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.05`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "DEADPAN_REACTION",
  "secondary_mechanisms": [
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "High-stakes absurdity receives a restrained response."
}
```

---

### Passage 155 [PARTIAL] — *Three Men In A Boat* (`three_men_in_a_boat_ch11_05264`)

> "Oh! that's where it is, is it?," replied the man; "well, you take my
advice and go there quietly, and take that watch of yours with you; and
don't let's have any more of it.

- **Detector Prediction:** `PARTIAL` | Stratum: `REJECT` | Primary: `DEADPAN_REACTION` (conf: `0.25`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [
    "MISUNDERSTANDING",
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Repeated misunderstandings make the original problem progressively more absurd."
}
```

---

### Passage 156 [NO_CONTROL] — *A Damsel In Distress* (`a_damsel_in_distress_ch21_03336`)

> Target Emotion: Hopeful / Reassuring | Valence: 0.23
CHAPTER XVIII  THE VOICE PROM THE PAST  The library, whither Jimmy had made his way after leaving Mrs

- **Detector Prediction:** `NO` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.0`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 5,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "No clear comedy craft."
}
```

---

### Passage 157 [NO_CONTROL] — *Idle Thoughts* (`idle_thoughts_chNone_02601`)

> And I presume you know what that unfortunate movement led to? As for the particular locality in which the hand-bag was found, a cloak-room at a railway station might serve to conceal a social indiscretion - has probably, indeed, been used for that purpose before now - but it could hardly be regarded as an assured basis for a recognised position in good society

- **Detector Prediction:** `NO` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.0`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "STATUS_REVERSAL",
  "secondary_mechanisms": [
    "DEADPAN_REACTION",
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Expected authority is quietly displaced, creating a strong status joke."
}
```

---

### Passage 158 [NO_CONTROL] — *Jill The Reckless* (`jill_the_reckless_chNone_09908`)

> **Story Outline for Jill The Reckless**

- **Hook**: CHAPTER I
- **Midpoint**: CHAPTER VII

A YOUNG KNIGHT-ERRANT.

I would gladly have left the two together, and gone straight in
- **Climax**: But I cried, "What of that?  You were taken by treachery!  Your safe conduct was disregarded

- **Detector Prediction:** `NO` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.0`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [
    "MISUNDERSTANDING"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 8,
  "craft_clarity": 8,
  "training_value": 8,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Semantic ambiguity/literalism creates the joke."
}
```

---

### Passage 159 [NO_CONTROL] — *Love Among The Chickens* (`love_among_the_chickens_ch16_10052`)

> "Shine!," With the
ignorant innocence of a child or a savage, who believe everything
possible, Yanson felt like crying to the sun: He begged, he
implored that the sun should shine, but the night drew its long, dark
hours remorselessly over the earth, and there was no power that could
hasten its course.

- **Detector Prediction:** `NO` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.0`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "PARTIAL",
  "craft_stratum": "REJECT",
  "primary_mechanism": "SOCIAL_EMBARRASSMENT",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 7,
  "craft_clarity": 4,
  "training_value": 4,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Embarrassment is plausible but incomplete."
}
```

---

### Passage 160 [NO_CONTROL] — *My Man Jeeves* (`my_man_jeeves_ch12_02198`)

> Speaker: If | Target Emotion: Urgent / Cautious
"said Voules," "I beg your pardon, sir, If it would be convenient I should be glad to have the afternoon off.

- **Detector Prediction:** `NO` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.0`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "PHYSICAL_COMPLICATION",
  "secondary_mechanisms": [
    "ESCALATION",
    "MISUNDERSTANDING"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 10,
  "craft_clarity": 10,
  "training_value": 10,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Strong physical farce with multiple interacting complications."
}
```

---

### Passage 161 [NO_CONTROL] — *Piccadilly Jim* (`piccadilly_jim_chNone_02769`)

> The sight threw me into a passion, and I profanely said to myself while I was dressing, "The next time I see Father Deveaux, I will give my tongue full swing, and make the hair of that holy man stand on end with terror!" A few hours afterwards, he came to the convent, and all my resolution melted away at the sight of him

- **Detector Prediction:** `NO` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.0`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 5,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": true,
  "notes": "Serious passage without a comic engine."
}
```

---

### Passage 162 [NO_CONTROL] — *Psmith In The City* (`psmith_in_the_city_ch1_08970`)

> MEASURE FOR MEASURE *** Executive Director's Notes: In addition to the notes below, and so you will *NOT* think all
the spelling errors introduced by the printers of the time have
been corrected, here are the first few lines of Hamlet, as they
are presented herein: Barnardo. Who's there?
  Fran. Nay answer me: Stand & vnfold
your selfe Bar. Long liue the King *       *       *       *       * As I understand it, the printers often ran out of certain words
or letters they had often packed into a "cliche". . .this is the
original meaning of the term cliche. . .and thus, being unwilling
to unpack the cliches, and thus you will see some substitutions
that look very odd. . .such as the exchanges of u for v, v for u,
above. . .and you may wonder why they did it this way, presuming
Shakespeare did not actually write the play in this manner. . . . The answer is that they MAY have packed "liue" into a cliche at a
time when they were out of "v"'s. . .possibly having used "vv" in
place of some "w"'s, etc.  This was a common practice of the day,
as print was still quite expensive, and they didn't want to spend
more on a wider selection of characters than they had to. You will find a lot of these kinds of "errors" in this text, as I
have mentioned in other times and places, many "scholars" have an
extreme attachment to these errors, and many have accorded them a
very high place in the "canon" of Shakespeare.  My father read an
assortment of these made available to him by Cambridge University
in England for several months in a glass room constructed for the
purpose.  To the best of my knowledge he read ALL those available
. . .in great detail. . .and determined from the various changes,
that Shakespeare most likely did not write in nearly as many of a
variety of errors we credit him for, even though he was in/famous
for signing his name with several different spellings. So, please take this into account when reading the comments below
made by our volunteer who prepared this file:  you may see errors
that are "not" errors. . . . So. . .with this caveat. . .we have NOT changed the canon errors,
here is the Project Gutenberg Etext of Shakespeare's play. Michael S. Hart
Project Gutenberg
Executive Director *       *       *       *       * Scanner's Notes: What this is and isn't. This was taken from a copy of
Shakespeare's first folio and it is as close as I can come in
ASCII to the printed text. The elongated S's have been changed to small s's and the
conjoined ae have been changed to ae. I have left the spelling,
punctuation, capitalization as close as possible to the printed
text. I have corrected some spelling mistakes (I have put
together a spelling dictionary devised from the spellings of
the Geneva Bible and Shakespeare's First Folio and have unified
spellings according to this template), typo's and expanded
abbreviations as I have come across them. Everything within
brackets [] is what I have added. So if you don't like that you
can delete everything within the brackets if you want a purer
Shakespeare. Another thing that you should be aware of is that there are
textual differences between various copies of the first folio. So
there may be differences (other than what I have mentioned above)
between this and other first folio editions. This is due to the
printer's habit of setting the type and running off a number of
copies and then proofing the printed copy and correcting the type
and then continuing the printing run. The proof run wasn't thrown
away but incorporated into the printed copies. This is just the
way it is. The text I have used was a composite of more than 30
different First Folio editions' best pages. David Reed

- **Detector Prediction:** `NO` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.0`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [
    "DEADPAN_REACTION",
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "The comic problem keeps growing while narration remains restrained."
}
```

---

### Passage 163 [NO_CONTROL] — *Right Ho* (`right_ho_ch9_04881`)

> "Good night," It was working along into the small hours now, but I thought I might as well make a night of it and finish the thing up, so I rang up an hotel near the Strand.

- **Detector Prediction:** `NO` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.0`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "PARTIAL",
  "craft_stratum": "REJECT",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 7,
  "craft_clarity": 4,
  "training_value": 4,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Witty fragment but weak as a standalone training example."
}
```

---

### Passage 164 [NO_CONTROL] — *Something Fresh* (`something_fresh_ch4_02128`)

> "Next!," It was not until the hands of the fat clock
over the door pointed to twenty minutes past eleven that the
office boy's found him the only survivor.

- **Detector Prediction:** `NO` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.0`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "DIALOGUE_SUBTEXT",
  "secondary_mechanisms": [
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "The comic meaning is carried by what the speakers avoid saying."
}
```

---

### Passage 165 [NO_CONTROL] — *The Adventures Of Sally* (`the_adventures_of_sally_ch10_05914`)

> "The memory of the just is blessed," It is sweet to recall any
incident in the life of him who will ever live in the hearts of many.

- **Detector Prediction:** `NO` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.0`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [
    "VERBAL_WIT",
    "SOCIAL_EMBARRASSMENT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "A mistaken interpretation causes both verbal and social comic consequences."
}
```

---

### Passage 166 [NO_CONTROL] — *The Click Of Triangle* (`the_click_of_triangle_chNone_00108`)

> And this is true: I like not the humor of lying: hee hath wronged mee in some humors: I should haue borne the humour'd Letter to her: but I haue a sword: and it shall bite vpon my necessitie: he loues your wife; There's the short and the long: My name is Corporall Nim: I speak, and I auouch; 'tis true: my name is Nim: and Falstaffe loues your wife: adieu, I loue not the humour of bread and cheese: adieu  Page

- **Detector Prediction:** `NO` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.0`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "PHYSICAL_COMPLICATION",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 4,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Physical action is not comic craft."
}
```

---

### Passage 167 [NO_CONTROL] — *The Diary Of A Nobody* (`the_diary_of_a_nobody_ch2_00926`)

> "Mosaic record," Gladstone is of opinion that the was meant to give moral, and not scientific, instruction to those for whom it was written, they may be disposed to think that I must be misleading them.

- **Detector Prediction:** `NO` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.0`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [
    "STATUS_REVERSAL",
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Sharp dialogue overturns the expected interpersonal position."
}
```

---

### Passage 168 [NO_CONTROL] — *The Inimitable Jeeves* (`the_inimitable_jeeves_chNone_04732`)

> The Court of Aldermen had agreed that each of their number should on the Saturday night make the round of his ward and select "fifty, forty, twenty, or ten" tall and comely men, who should be warned in the king's name to appear the next morning before seven o'clock at the Guildhall

- **Detector Prediction:** `NO` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.0`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [
    "PHYSICAL_COMPLICATION",
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 10,
  "craft_clarity": 10,
  "training_value": 10,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Excellent farcical escalation."
}
```

---

### Passage 169 [NO_CONTROL] — *The Little Nugget* (`the_little_nugget_chNone_00236`)

> Pets thim animals may be, an' domestic they be, but pigs I'm blame sure they do be, an' me rules says plain as the nose on yer face, 'Pigs Franklin to Westcote, thirty cints each

- **Detector Prediction:** `NO` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.0`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "PARTIAL",
  "craft_stratum": "REJECT",
  "primary_mechanism": "CALLBACK",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LONG_HORIZON",
  "setup_accurate": true,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 7,
  "craft_clarity": 4,
  "training_value": 3,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Callback depends on context beyond the excerpt."
}
```

---

### Passage 170 [NO_CONTROL] — *The Man Upstairs* (`the_man_upstairs_ch7_06325`)

> Speaker: Clair | Target Emotion: Urgent / Cautious
"said that gentleman, rising," Clair, the directors of the Elevated are in session, and we must hurry.

- **Detector Prediction:** `NO` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.0`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "The misunderstanding is clean and pedagogically useful."
}
```

---

### Passage 171 [NO_CONTROL] — *The Prince And Betty* (`the_prince_and_betty_chNone_02770`)

> Accuse me not, beseech thee, that I wear Too calm and sad a face in front of thine; For we two look two ways, and cannot shine With the same sunlight on our brow and hair

- **Detector Prediction:** `NO` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.0`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "DEADPAN_REACTION",
  "secondary_mechanisms": [
    "VERBAL_WIT",
    "ESCALATION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Underreaction makes a worsening absurdity funnier."
}
```

---

### Passage 172 [NO_CONTROL] — *Their Mutual Child* (`their_mutual_child_ch8_01105`)

> "Sir, I am a tourist!," Supposing his father asked him, on his return,
what equivalent he had brought back for the time and money put into his
experiment! The only possible answer would be:.

- **Detector Prediction:** `NO` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.0`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 5,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Expository/historical material."
}
```

---

### Passage 173 [NO_CONTROL] — *Three Men In A Boat* (`three_men_in_a_boat_ch14_02284`)

> "owner having no further use for same," He did make one
or two feeble efforts to take up the work again when the six months
had elapsed, but there was always the same coldness - the same want of
sympathy on the part of the world to fight against; and, after awhile,
he despaired altogether, and advertised the instrument for sale at a
great sacrifice - and took to
learning card tricks instead.

- **Detector Prediction:** `NO` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.0`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "SOCIAL_EMBARRASSMENT",
  "secondary_mechanisms": [
    "MISUNDERSTANDING",
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Social embarrassment emerges from a misunderstanding and is reinforced by dry dialogue."
}
```

---

### Passage 174 [NO_CONTROL] — *Three Men On The Bummel* (`three_men_on_the_bummel_chNone_01076`)

> In a German park I have seen a gardener step gingerly with felt boots on to grass-plot, and removing therefrom a beetle, place it gravely but firmly on the gravel; which done, he stood sternly watching the beetle, to see that it did not try to get back on the grass; and the beetle, looking utterly ashamed of itself, walked hurriedly down the gutter, and turned up the path marked "Ausgang

- **Detector Prediction:** `NO` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.0`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "STATUS_REVERSAL",
  "secondary_mechanisms": [
    "DEADPAN_REACTION",
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 10,
  "craft_clarity": 10,
  "training_value": 10,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Clear hierarchy reversal with an understated payoff."
}
```

---

### Passage 175 [NO_CONTROL] — *Uneasy Money* (`uneasy_money_ch2_02857`)

> Prologue As of old Phoenician men, to the Tin Isles sailing
     Straight against the sunset and the edges of the earth,
     Chaunted loud above the storm and the strange sea's wailing,
     Legends of their people and the land that gave them birth--
     Sang aloud to Baal-Peor, sang unto the horned maiden,
     Sang how they should come again with the Brethon treasure laden,
     Sang of all the pride and glory of their hardy enterprise,
     How they found the outer islands, where the unknown stars arise;
     And the rowers down below, rowing hard as they could row,
     Toiling at the stroke and feather through the wet and weary weather,
     Even they forgot their burden in the measure of a song,
     And the merchants and the masters and the bondsmen all together,
     Dreaming of the wondrous islands, brought the gallant ship along;
     So in mighty deeps alone on the chainless breezes blown
     In my coracle of verses I will sing of lands unknown,
     Flying from the scarlet city where a Lord that knows no pity,
     Mocks the broken people praying round his iron throne,
     Sing about the Hidden Country fresh and full of quiet green.
     Sailing over seas uncharted to a port that none has seen.

- **Detector Prediction:** `NO` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.0`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "PARTIAL",
  "craft_stratum": "REJECT",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 7,
  "craft_clarity": 4,
  "training_value": 4,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "Some progression, but not a sufficiently clear comic escalation."
}
```

---

### Passage 176 [NO_CONTROL] — *A Damsel In Distress* (`a_damsel_in_distress_chNone_03792`)

> Having turned slowly so that his eyes rested on Lord Wisbeach's ingenuous countenance, Willie paused, and his face assumed the expression of his photograph in the _Chronicle_

- **Detector Prediction:** `NO` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.0`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "PHYSICAL_COMPLICATION",
  "secondary_mechanisms": [
    "ESCALATION",
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Physical mishap is deliberately escalated and verbally framed."
}
```

---

### Passage 177 [NO_CONTROL] — *Idle Thoughts* (`idle_thoughts_chNone_07051`)

> Cecily, mamma, whose views on education are remarkably strict, has brought me up to be extremely short-sighted; it is part of her system; so do you mind my looking at you through my glasses? CECILY

- **Detector Prediction:** `NO` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.0`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "MISUNDERSTANDING",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 5,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": true,
  "notes": "No clear comic craft."
}
```

---

### Passage 178 [NO_CONTROL] — *Jill The Reckless* (`jill_the_reckless_ch11_03183`)

> "my companion added bitterly," Do you not see, Anne? to
kill me at once were too small a revenge for him! He must torture
me--or rather he would if he could--by the pains of anticipation.

- **Detector Prediction:** `NO` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.0`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Strong compact verbal comedy."
}
```

---

### Passage 179 [NO_CONTROL] — *Love Among The Chickens* (`love_among_the_chickens_chNone_05017`)

> "  They were riding thus in order to appear two hours later face to face before the inexplicable great mystery, in order to pass from Life to Death - and they were introducing each other

- **Detector Prediction:** `NO` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.0`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "YES",
  "craft_stratum": "COMPOSITE_CRAFT",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [
    "MISUNDERSTANDING",
    "DEADPAN_REACTION"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 9,
  "keep_verdict": "KEEP",
  "detector_correct": false,
  "notes": "Repeated complications and restrained reaction form the comic engine."
}
```

---

### Passage 180 [NO_CONTROL] — *My Man Jeeves* (`my_man_jeeves_ch14_04030`)

> "I said," " "But one moment, I'd be delighted to be of any use to you, but in a purely family affair like this, wouldn't it be better - in fact, how about tackling old Bill on the subject?" "I have asked Bill already.

- **Detector Prediction:** `NO` | Stratum: `REJECT` | Primary: `MISUNDERSTANDING` (conf: `0.0`)
- **Temporal Horizon:** `LOCAL` | Secondary: `[]`

```json
{
  "craft_presence": "NO",
  "craft_stratum": "REJECT",
  "primary_mechanism": "VERBAL_WIT",
  "secondary_mechanisms": [],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": false,
  "escalation_accurate": false,
  "reversal_accurate": false,
  "payoff_accurate": false,
  "literary_quality": 5,
  "craft_clarity": 1,
  "training_value": 1,
  "keep_verdict": "REJECT",
  "detector_correct": false,
  "notes": "No self-contained comic mechanism."
}
```

---

