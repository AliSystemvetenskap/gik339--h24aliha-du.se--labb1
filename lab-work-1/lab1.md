---
title: "Lab Work 1 – StarkFit Gyms"
subtitle: "Defining our company and project"
---

**Course:** IT Architecture (HT26), Dalarna University\
**Group:** 15\
**Members:** Ali Hasan, Bilal Ahmed Adem\
**Date:** 2026-11-10

# 1. Our group and our idea

We are a group of two, Ali and Bilal. For this course we chose to base our work on a gym chain. Most people have been to a gym, so the business is easy to understand. At the same time, a gym chain has many systems that need to work together: memberships, door access, class booking, payments and apps. That makes it a good case for IT architecture.

The company is not real. We made it up, but we tried to make it as realistic as possible.

# 2. The company

**StarkFit AB** is a Swedish gym chain with its head office in Borlänge. It offers gym training, group classes (like spinning, yoga and HIIT) and personal training.

| Fact | Details |
|---|---|
| Founded | 2015 in Borlänge |
| Gyms | 25 gyms in Dalarna, Gävleborg, Värmland and Uppsala |
| Members | About 40 000 |
| Employees | About 180 (head office, gym staff, trainers, many part-time) |
| Memberships | Monthly direct debit, yearly card, student and day passes |
| How it grew | Started with 12 gyms, then bought *GymNorr* (8 gyms) in 2022 and *FlexTräning* (5 gyms) in 2024 |

# 3. The project

## The problem today

StarkFit grew mainly by buying other gym chains. Each chain came with its own systems, and these were never properly joined together. Today the company runs:

- **three different membership systems**, one for each original chain,
- **two different door systems**, key tags in some gyms and QR codes in the app in others,
- **two booking apps** for group classes,
- **payments spread out** over direct debit, card payments and invoices, handled differently depending on the system.

This causes real problems for both members and the company:

- A member who joined in Borlänge **cannot get into** a former GymNorr gym in Gävle, even though StarkFit promises "train at all our gyms".
- The same person can exist **two or three times** in different systems, so nobody knows the true number of members.
- Head office builds its monthly reports **by hand** from three systems, and the numbers often do not match.
- When a member quits, their personal data is not always deleted from the old systems, which is a **GDPR risk**.
- Every January, when many people join at once, the old systems **become slow** or crash.

These problems cannot be fixed by simply buying a new app. The gyms must stay open, the doors must keep working, and money must keep coming in while the systems are changed.

## Our project: "One Member"

The project is to **design a new IT architecture for StarkFit**, where every member exists only once and can use every gym. We call it *One Member*. At its centre is one shared member register. The door system, class booking, payments, the member app and head-office reports all connect to it. The old systems will be phased out **one gym group at a time**, so the business never has to stop.

## Scope

**Included in the project:**

- A plan for how the company's business, data and systems fit together.
- One shared member register, with old member data merged and duplicates removed.
- Connecting door access, class booking and payments to the new register.
- One member app and website for all gyms.
- Automatic reports for head office and gym managers.
- A step-by-step plan for moving each gym over from its old system.

**Not included:**

- Salaries and accounting. These stay with the external accounting firm.
- New gym equipment or new gyms.
- Marketing campaigns.

## Goals

1. **One member, all gyms.** By the end of 2027, every member can enter all 25 gyms with the same card or app.
2. **No duplicates.** Each person is registered only once in the member register.
3. **No stop for members.** Door access and class booking should not be down for more than one hour during any gym's switch to the new system.
4. **Handle the January rush.** The system should cope with three times the normal number of sign-ups without slowing down.
5. **Reports without manual work.** Head office gets correct monthly reports on members, visits and income automatically.
6. **Safe personal data.** Member data is stored safely and deleted on time, according to GDPR.

# 4. Stakeholders

A stakeholder is any person or group that affects the project or is affected by it (Freeman, 1984).

| Stakeholder | What they want | How the project affects them |
|---|---|---|
| **Members** | Train at any gym, easy booking, correct payments | One card/app that works everywhere |
| **Owners and management** | Growth, profit, a clear picture of the business | Reliable numbers and lower system costs |
| **Gym managers** | Running their gym smoothly, happy members | Fewer complaints, easy access to their own figures |
| **Reception and trainers** | Quick help for members, simple class lists | One system instead of three |
| **Head office (IT, finance, customer service)** | Systems that work and match each other | Less manual work, but a big change to manage |
| **Suppliers of current systems** | Keep their contracts | Some contracts will end |
| **Payment partners** (bank, Autogiro, card provider) | Correct and secure payment data | Payments move to one system |
| **Door system supplier** | Clear technical needs | Doors must connect to the new member register |
| **Authorities** (GDPR, IMY) | Personal data is protected | Data must be stored and deleted correctly |

# 5. Company structure

StarkFit is organised with a small head office and a regional structure. Mintzberg (1979) would describe this as a *divisional* type of structure, where each region and gym runs its daily work, while head office decides strategy and shared services.

| Level | Roles | Main tasks |
|---|---|---|
| **Management** | CEO, CFO, Head of Operations | Strategy, budget, buying new gyms |
| **Head office functions** | IT (4), Finance (3), Customer service (5), Marketing (3), HR (2) | Shared systems, payments, support, campaigns, staff |
| **Regional managers** | 4 regions | Follow up on the gyms in their region |
| **Gym managers** | 1 per gym | Daily running of the gym, staff schedules |
| **Gym staff** | Reception, trainers, personal trainers | Meeting members, classes, training |

The IT team leads the *One Member* project, with support from finance, customer service and a group of gym managers who test each step in practice.

# 6. Main processes

A business process is a set of steps that together create value for a customer (Dumas et al., 2018). These are the main processes the new architecture must support.

## 6.1 Becoming a member

1. The person chooses a membership in the app, on the website or at the reception.
2. They fill in their details and accept the terms.
3. They choose how to pay (direct debit, card or invoice).
4. The member is saved in the member register and gets a key tag or app access.

## 6.2 Visiting a gym

1. The member scans their tag or app at the door.
2. The door system checks with the member register that the membership is active.
3. The door opens, and the visit is saved.

## 6.3 Booking a class

1. The member books a class in the app.
2. The system checks that there are free spots and that the membership includes classes.
3. The trainer sees the list of booked members. No-shows are noted.

## 6.4 Monthly payment

1. Each month, the system creates payments for all active members.
2. Payments are sent to the bank or card provider.
3. If a payment fails, the member gets a reminder, and access may be paused.

## 6.5 Ending a membership

1. The member cancels in the app or at reception.
2. Access stops when the notice period ends.
3. Personal data is deleted or anonymised after the time required by law.

## 6.6 Moving a gym to the new system

1. Member data from the gym's old system is copied and cleaned.
2. Duplicates are found and merged with existing members.
3. The door and booking systems at the gym are connected to the new register.
4. The gym is tested for a few days before the old system is turned off.

# 7. Focus of the project

The main focus is **how StarkFit's business, data and systems fit together**. Ross, Weill and Robertson (2006) describe enterprise architecture as the plan that links a company's business processes with its IT. Because StarkFit has to connect many old and new systems, we will also look at integration, meaning how systems exchange data with each other (Hohpe & Woolf, 2003).

In the coming labs we will use StarkFit for each area of IT architecture in the course:

- **Business architecture.** Goals, stakeholders, structure and processes (this document).
- **Data modeling.** Members, memberships, gyms, visits, classes, bookings and payments.
- **System architecture.** How the member register connects to doors, booking, payments and the old systems.
- **Web information architecture.** How the member app and website are organised.
- **Platform architecture.** Where the systems run, and how they handle peaks like the January rush.

We will try to use open standards where possible, for example for exchanging data with door systems and payment partners, in line with frameworks such as TOGAF (The Open Group, 2018).

# 8. Summary

StarkFit grew by buying other gym chains and now runs three membership systems that do not work together. Our project, *One Member*, will give StarkFit a new IT architecture with one member register at its centre, introduced one gym group at a time. We will keep using StarkFit for the rest of the course.

# References

Dumas, M., La Rosa, M., Mendling, J., & Reijers, H. A. (2018). *Fundamentals of Business Process Management* (2nd ed.). Springer.

European Union. (2016). *Regulation (EU) 2016/679 of the European Parliament and of the Council (General Data Protection Regulation)*. Official Journal of the European Union, L 119.

Freeman, R. E. (1984). *Strategic Management: A Stakeholder Approach*. Pitman.

Hohpe, G., & Woolf, B. (2003). *Enterprise Integration Patterns: Designing, Building, and Deploying Messaging Solutions*. Addison-Wesley.

Mintzberg, H. (1979). *The Structuring of Organizations*. Prentice-Hall.

Ross, J. W., Weill, P., & Robertson, D. C. (2006). *Enterprise Architecture as Strategy: Creating a Foundation for Business Execution*. Harvard Business School Press.

The Open Group. (2018). *The TOGAF Standard, Version 9.2*. The Open Group.
