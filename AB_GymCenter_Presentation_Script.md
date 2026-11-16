# AB GymCenter – Presentation Script (Group 15)

**Speakers:** Ali Hasan (slides 1–6) · Bilal Ahmed Adem (slides 7–13)
**Total time:** ~10 minutes (Ali ≈ 5 min, Bilal ≈ 5 min)

---

## Slide 1 – Title (Ali, ~30 s)

Hi everyone. We are Group 15. My name is Ali Hasan.

*(Bilal:)* And I'm Bilal Ahmed Adem.

*(Ali:)* Today we will present AB GymCenter. It's the company we made up for this course. We'll talk about the company, the project, the stakeholders, how the company is organized, and how it works. At the end we show it with an enterprise architecture view and a process model. We have both been gym members, so we based it on how a real gym works day to day.

## Slide 2 – Who we are (Ali, ~45 s)

AB GymCenter is a medium-sized gym in Stockholm. It was started in 2018 by two personal trainers. They wanted a gym that feels friendly and isn't too expensive.

Today we have one big location, about 2,000 square metres. We have around 3,500 members and 28 employees, and we are open every day from five in the morning to eleven at night.

Our vision is simple: **make it easy for everyone in the city to stay healthy.**

## Slide 3 – Products and services (Ali, ~45 s)

We sell four kinds of products and services.

The biggest one is the **gym membership**. It's paid every month and it brings in about 75 percent of our income.

Then we have **group classes** like yoga, spinning and HIIT, **personal training** packages, and a small **shop** with drinks and supplements. Those three bring in the other 25 percent.

Most of our members are students and young workers between 18 and 40. We also have older members who mostly come to the daytime classes.

## Slide 4 – The problem today (Ali, ~50 s)

The problem is that AB GymCenter still works in an old way.

Members book classes on an old website. The reception keeps paper lists. Member data, payments and staff schedules are kept in different Excel files that don't talk to each other.

Because of this, classes are often overbooked or almost empty. The reception spends a lot of time answering simple questions like "is there space in spinning tonight?". And many members leave after only a few months.

So the management decided to start a project to replace all of this with one digital system.

## Slide 5 – The project (Ali, ~50 s)

The project is called the **Member App and Booking System**.

For members, there is a mobile app and a web page. They can sign up, pay, book classes and trainers, check in at the door with a QR code, and see their training history.

For the staff, there is an admin system to manage members, schedules, trainers and payments. It connects to a payment provider and to the door system. Management also gets simple reports on visits, busy hours and cancellations.

What is **not** in the project: opening a second gym, buying new equipment, or building an online video service. We can look at those later.

## Slide 6 – SMART goals (Ali, ~50 s)

We wrote our goals in a SMART way, so they are specific and measurable.

One: within six months after launch, **80 percent** of all class bookings should be made in the app.

Two: within one year, the reception's admin time should go down by **30 percent**.

Three: the yearly cancellation rate should drop from **28 to 20 percent**.

And four: average class attendance should go up from **60 to 80 percent** of the available places.

Now Bilal will talk about the people and the structure behind the company.

---

## Slide 7 – Stakeholders (Bilal, ~50 s)

Thanks Ali. A stakeholder is anyone who can affect the project or is affected by it.

Our **primary** stakeholders are directly involved. That's the members, who want easy booking, a fair price and safe data. The owners and management, who want more profit and fewer cancellations. The reception staff, who want less manual work. The trainers, who want clear schedules. And the project team and IT, who need clear requirements, time and money.

Our **secondary** stakeholders are more indirect. The app developer, the payment provider, suppliers, the authorities, who make sure we follow GDPR, and competing gyms. They are not involved, but they affect prices and what members expect.

## Slide 8 – Organization structure (Bilal, ~45 s)

AB GymCenter has a simple, functional structure with a short line between management and staff.

The general manager leads four departments. **Operations and Facility** with 6 people – opening, cleaning, equipment and safety. **Training and Classes**, our biggest team with 12 trainers. **Sales, Customer Service and Marketing** with 6 people, which includes the reception. And **Finance, HR and IT** with 3 people plus the general manager.

The project is led by a project manager from Finance, HR and IT. They report directly to the general manager and work with one person from each department.

## Slide 9 – Business processes (Bilal, ~50 s)

We split our processes into core processes, which create value for members, and support processes, which keep the company running.

We have four core processes. **Getting a new member** – from interest, to a free trial, to sign-up and monthly payment. **Booking and attending classes** – this one causes the most problems today, so it's the main target of the project. **Personal training** – first meeting, a training plan, sessions and follow-up. And the **daily running of the gym**.

The support processes are billing and payments, HR and staff scheduling, maintenance and purchasing, marketing, and IT and data handling, which includes backups and GDPR.

## Slide 10 – Perspectives (Bilal, ~40 s)

Different groups look at the company in different ways.

**Customers** want it to be easy – book in a few seconds, pay a fair price, and know their data is safe.

**Employees** want less paperwork and clear schedules, so they can spend time with members instead.

**Managers** want fewer cancellations, more profit and a clear view of the business through reports.

And the **sponsors**, the owners who pay for the project, want it delivered on time and on budget, and to pay back through more members staying longer.

## Slide 11 – Enterprise architecture view (Bilal, ~50 s)

To describe the company, we use an enterprise architecture view with three layers.

On top is the **business layer**: our members, our staff and the core processes we just talked about.

In the middle is the **application layer**: the member app, the web page, the admin system and the management reports. This layer also connects to two outside systems – the payment provider and the door system with QR check-in.

At the bottom is the **technology layer**: cloud hosting, the database, backups and security for GDPR.

The point is that everything is in one system instead of an old website, paper and Excel files.

## Slide 12 – Process model: Book and attend a class (Bilal, ~40 s)

Here is our main process as a simple BPMN-style model with three lanes: trainer, member and system.

The trainer plans a class and the schedule is published. The member books a place, and the system sends a reminder before the class. The member checks in at the door with the QR code. After the class, attendance is saved automatically. If a member doesn't show up several times, the system flags it and the reception can contact them.

This directly supports our goals about bookings in the app and higher attendance.

## Slide 13 – Success factors and next steps (Bilal, ~40 s)

To succeed, a few things are critical. Members must actually **use the app**. The system must be **easy for staff**. The **payment and door integrations** must be reliable. And we must follow **GDPR**.

For the rest of the course we will build on this. We'll connect the goals to a business model, model the membership and booking processes in BPMN, look at what data we need and how it's protected, and turn the stakeholders' needs into requirements and risks.

*(Both:)* Thank you for listening. Do you have any questions?
