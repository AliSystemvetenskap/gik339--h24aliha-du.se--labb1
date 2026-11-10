---
title: "Seminar 1 – Speaker Script"
subtitle: "StarkFit · Group 15 · Ali Hasan & Bilal Ahmed Adem"
---

**Total time:** 15 minutes + 5 minutes questions. **Ali:** slides 1–7 (about 7½ min). **Bilal:** slides 8–14 (about 7½ min).

Tip: don't read word for word. Know the main point of each slide and say it in your own words.

## Slide 1 – StarkFit  (Ali)

Hi everyone. We are group 15, I’m Ali and this is Bilal. Our company for this course is StarkFit, a gym chain we made up. Our project is called One Member. It is about giving StarkFit a new IT architecture so all its gyms and systems work together. I will start with the company, its products, the problem and the people involved. Then Bilal will show how the company is organised, its processes and our two architecture models.

## Slide 2 – StarkFit at a glance  (Ali)

StarkFit is a Swedish gym chain with its head office in Borlänge. It started in 2015 and today has 25 gyms, about 40,000 members and 180 employees. The important part is how it grew. It started with 12 gyms, then bought two smaller chains, GymNorr with 8 gyms and FlexTräning with 5. This is where our problem comes from, which I will get to in a minute. The company is made up, but we tried to make it realistic.

## Slide 3 – What StarkFit sells  (Ali)

StarkFit’s products fall into three categories. First, memberships: monthly with direct debit, a yearly card, a student membership and day passes. Second, training: the gym floor, which is open from five in the morning to eleven at night, group classes like spinning, yoga and HIIT, and personal training. Third, some extras, like training plans in the app and drinks and supplements sold at reception. The membership is the core product. Everything else depends on knowing who the member is and what they have paid for.

## Slide 4 – Three chains, three sets of systems  (Ali)

So what is the problem? Each chain StarkFit bought came with its own systems, and they were never joined together. Today StarkFit runs three membership systems, two door systems, two booking apps and three different ways of handling payments. This causes real problems. A member who joined in Borlänge can’t get into a former GymNorr gym in Gävle, even though StarkFit says you can train everywhere. The same person can exist two or three times, so nobody knows the real number of members. Head office builds reports by hand. Old member data is not always deleted, which is a GDPR risk. And every January, when lots of people join, the systems slow down. This can’t be fixed by just buying a new app, because the gyms must stay open and the doors must keep working while we change things.

## Slide 5 – One member register, every gym  (Ali)

Our project is called One Member. The idea is simple: every member should exist only once, and be able to use every gym. At the centre is one shared member register. The doors, class booking, payments, the app and the reports all connect to it. We don’t switch everything at once. We move one gym group at a time, so the business never stops. We set six goals, and each one can be measured. All 25 gyms open to every member by the end of 2027. Zero duplicate members. Doors and booking can’t be down for more than one hour when a gym switches. The system must handle three times the normal sign-ups in January. Reports should be created automatically. And personal data of people who leave must be deleted on time, according to GDPR.

## Slide 6 – Who has an interest in StarkFit  (Ali)

These are StarkFit’s key stakeholders. We use Freeman’s definition: anyone who affects the company or is affected by it. The most important are the members, because they pay for everything, and the owners, who want growth and profit. Inside the company we have managers, gym staff and the head office teams like IT and finance. Outside the company we have the system suppliers, where some contracts will end with our project, payment partners like the bank and card provider, and the authorities, since StarkFit handles a lot of personal data and must follow GDPR.

## Slide 7 – How each group sees StarkFit  (Ali)

Here are four perspectives on the company. Customers think: I pay for all gyms, so let me use all of them, with one app and correct bills. Employees, like reception staff, want to find a member in one system instead of three, so they can spend time helping people. Managers want correct numbers on members, visits and income, so they can compare gyms and make decisions. And the sponsors, which are the owners who pay for the project, want lower system costs, since today they pay for many systems, and a platform that makes it easy to buy and add more gyms in the future. Now Bilal will take over and show how StarkFit is organised.

## Slide 8 – Head office plus four regions  (Bilal)

Thanks Ali. This is how StarkFit is organised. At the top is the management team: the CEO, the CFO and the Head of Operations. Under them there are two parts. On the left, the head office, with shared services for all gyms: IT with four people, finance, customer service, marketing and HR. The IT team leads our One Member project. On the right, operations. Four regional managers each follow up a group of gyms, every gym has its own gym manager, and under them are the receptionists, trainers and personal trainers. Mintzberg calls this a divisionalized form: each region and gym runs its daily work, while head office decides strategy and runs shared systems.

## Slide 9 – The member’s journey  (Bilal)

These are StarkFit’s main business processes. We describe them as the member’s journey. One: join, where you pick a membership, sign up and get access. Two: visit, where you scan your tag or app and the door checks that your membership is active. Three: book a class, and the trainer sees who is coming. Four: pay every month, and if a payment fails the member gets a reminder. Five: leave, where access stops and personal data is deleted on time. Every one of these steps needs the member register, which is why the project focuses on it. We also have one change process for the project itself: moving a gym to the new system. We copy the data, remove duplicates, connect the doors and booking, test, and only then turn the old system off.

## Slide 10 – Becoming a member  (Bilal)

Our first architecture model is a business process model in BPMN. It shows the process “becoming a member”. We have three lanes: the member, the StarkFit system and the payment provider. The member chooses a membership and fills in their details. Then the system makes a decision, shown by the diamond: has this person been registered before? This is important for us, because duplicate members are one of StarkFit’s biggest problems. If yes, the system uses the existing record. If no, it creates a new one. Then the payment provider sets up direct debit or card payment. Finally the system activates access, and the member can enter any gym. That’s the end event, the thick circle.

## Slide 11 – StarkFit after One Member  (Bilal)

Our second model is an enterprise architecture, using the four layers from TOGAF. It shows StarkFit after the One Member project. At the top, the business layer: members, gyms and staff, and the processes we just saw. Under it, the data layer: the main things the company needs to keep track of, like member, membership, gym, visit, class booking and payment. Then the application layer, with the member register in the middle, marked in orange, because every other application uses it: the app, door access, class booking, billing and reports. At the bottom, the technology layer: a cloud platform, an integration layer with APIs so old and new systems can talk to each other during the switch, the door controllers in the gyms, and the links to the bank and card provider. Each layer supports the one above it. This is the model we will build on in the coming labs.

## Slide 12 – What StarkFit must get right  (Bilal)

So what must StarkFit get right for this to succeed? We see five success factors. One: every member can actually use every gym, because that is the promise to the customer. Two: the doors and booking must never stop, even while we switch systems. A gym where members can’t get in is a big failure. Three: clean data, one person, one record. Four: staff who know and trust the new system, so training the staff is part of the project. And five: personal data that is safe and deleted on time, to follow GDPR.

## Slide 13 – StarkFit for the rest of the course  (Bilal)

To sum up: StarkFit grew by buying other gym chains, and now has systems that don’t work together. Our project, One Member, puts one member register at the centre and rolls it out one gym group at a time. We will keep using StarkFit for the rest of the course. In the coming labs we will build on today’s models: a data model for members, memberships, visits, bookings and payments; the system architecture, showing how the register connects to doors, booking and payments; the web information architecture of the app and website; and the platform architecture, where the systems run and how they handle the January rush.

## Slide 14 – Thank you – questions?  (Bilal)

That was our presentation of StarkFit and the One Member project. Thank you for listening. Here are our references. We are happy to take any questions.

# Likely questions and answers

**Why not just buy one new system and switch all gyms at once?**  
Because the gyms must stay open. If the doors or payments stop, members can't train and StarkFit loses money. Moving one gym group at a time lowers the risk, and we can test each step before turning an old system off.

**Who is the most important stakeholder?**  
The members, because they pay for everything and the whole project is about their promise: train at every gym. The owners are also key, because they are the sponsors who pay for the project.

**How do you know if the project succeeded?**  
We look at the measurable goals: all 25 gyms open to every member by the end of 2027, zero duplicate members, max one hour of downtime per gym switch, and automatic monthly reports.

**Why did you choose BPMN and TOGAF?**  
BPMN shows one process step by step, and who does what, which fits the problem with duplicate members. TOGAF's four layers give the big picture of how business, data, applications and technology fit together.

**What data will you model later?**  
Member, membership, gym, visit, class, booking and payment, and how they are connected. For example, one member has one membership but many visits and bookings.

**Why is GDPR important here?**  
StarkFit stores names, addresses, payment details and when people visit. Data of people who leave must be deleted on time, and today the old systems don't do that.