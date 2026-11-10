---
title: "Lab Work 1 – Kollekt Studio"
subtitle: "Defining our company and project"
---

**Course:** GIK2NV – Data storage and management technologies\
**Group:** 15\
**Members:** Ali Hasan, Bilal Ahmed Adem\
**Date:** 2026-11-10

# 1. Our group and why we chose this idea

We are a group of two, Ali and Bilal. For this course we chose to build our work around a small online clothing brand. We picked it because we already know a lot about e-commerce and online marketing, both from our own projects and from following brands we like. That makes it easier for us to describe how things really work day to day, which will help a lot when we build data models later in the course.

The company is not real. We made it up, but we tried to make it as realistic as possible.

# 2. The company

**Kollekt Studio AB** is a small Swedish streetwear brand based in Borlänge. It sells hoodies, t-shirts, sweatpants and caps. The style is simple and clean, with a focus on good quality cotton and limited drops.

Some quick facts about the company:

| Fact | Details |
|---|---|
| Founded | 2023 |
| Employees | 8 people (plus 2 part-time warehouse workers in busy periods) |
| Sales channels | Own webshop (about 85% of sales) and Instagram/TikTok shop |
| Customers | Mostly young adults aged 16–30 in Sweden and the Nordics |
| Yearly orders | Around 12 000 orders |
| Production | Clothes are made by a factory in Portugal. Printing is done in Sweden |

Kollekt Studio sells only online. Customers find the brand through social media, influencers and ads, and then buy through the webshop. The company releases new products in "drops" a few times a year. A drop is a small collection that is only available for a short time or until it sells out.

# 3. The project

## The problem today

The company has grown fast, but its systems have not kept up. Right now, information is spread across many places:

- Orders come in through the webshop platform.
- Stock levels are tracked in a shared Excel sheet that the warehouse updates by hand.
- Customer questions are handled in an email inbox and in Instagram messages.
- Supplier orders are kept in emails and PDF files.

Because nothing is connected, mistakes happen. Sometimes the webshop shows a product as in stock when it is actually sold out. Customer service can't easily see a customer's order history. During drops, when hundreds of orders come in within an hour, these problems get much worse.

## Our project: "One Place"

The project is to **build one central system where all important company data is stored and connected**. We call it *One Place*. It will hold information about products, stock, customers, orders, payments, returns and suppliers in one shared database. Every department will work from the same data.

## Scope

**Included in the project:**

- A central database for products, stock, customers, orders, returns and suppliers.
- Connecting the webshop so that orders and stock update automatically.
- Simple views for each team. For example, the warehouse sees what to pack, and customer service sees a customer's orders.
- Basic reports, such as best-selling products and stock that is running low.

**Not included:**

- Building a new webshop. We keep the one we have.
- Accounting and salaries. These stay with the external accounting firm.
- Marketing tools and ad platforms. We may connect them later, but not in this project.

## Goals

We want the goals to be clear and possible to measure:

1. **No more overselling.** Stock should update automatically, so that no product can be sold when it is out of stock.
2. **Faster customer service.** Customer service should be able to find any order in under one minute. The goal is to answer customers within 24 hours.
3. **Faster packing.** Orders should be ready to ship within one working day, even during drops.
4. **Better decisions.** Management should get a weekly report showing sales, stock and returns, without anyone building it by hand.
5. **Safe customer data.** All personal data should be stored safely and handled according to GDPR.

# 4. Stakeholders

A stakeholder is any person or group that affects the project or is affected by it (Freeman, 1984). For our project we found these:

| Stakeholder | What they want | How the project affects them |
|---|---|---|
| **Customers** | Correct stock information, fast delivery, easy returns | Fewer cancelled orders and faster answers |
| **Owners / founders** | Growth, profit and a good brand reputation | Better reports and fewer costly mistakes |
| **Customer service** | Quick access to order and customer information | Everything in one place instead of many inboxes |
| **Warehouse staff** | Clear packing lists and correct stock numbers | No more manual Excel updates |
| **Marketing team** | Know what sells and when to plan drops | Sales data they can trust |
| **Suppliers** (factory and printer) | Clear and correct purchase orders | Orders based on real stock levels |
| **Delivery partners** (PostNord, DHL) | Correct shipping information | Shipping data sent automatically |
| **Payment providers** (Klarna, card payments) | Correct payment and refund data | Payments linked to the right order |
| **Authorities** (GDPR rules) | Personal data is protected | The system must store data safely |

# 5. Company structure

Kollekt Studio is a small company with a simple and flat structure. Mintzberg (1979) calls this a *simple structure*, where the founders make most of the big decisions and people often help out across teams. Even so, each person has a clear main role.

| Team | People | Main tasks |
|---|---|---|
| **Management** (Founders / CEO) | 2 | Strategy, finance, product decisions, contact with suppliers |
| **Marketing & Social Media** | 2 | Ads, influencers, content, planning drops |
| **Customer Service** | 1 | Answering questions, handling returns and complaints |
| **Warehouse & Logistics** | 2 (+2 part-time) | Receiving stock, packing orders, shipping, returns |
| **E-commerce & IT** | 1 | Running the webshop, product pages, this project |

The two founders are in charge of everything. The other teams report directly to them. In the project, the E-commerce & IT person leads the work, and every team gives input on what they need.

# 6. Main processes

A business process is a set of steps that together create value for a customer (Dumas et al., 2018). These are the most important processes in Kollekt Studio, and they are the ones our new system needs to support.

## 6.1 Order process (the most important)

1. The customer picks products and places an order in the webshop.
2. The customer pays with card or Klarna.
3. The system saves the order and lowers the stock for those products.
4. The warehouse gets the order on its packing list.
5. The warehouse packs the order and books shipping with PostNord or DHL.
6. The customer gets an email with a tracking number.
7. The order is marked as delivered.

## 6.2 Return process

1. The customer asks for a return within 30 days.
2. The customer sends the product back.
3. The warehouse checks the product. If it is OK, it goes back into stock.
4. The customer gets their money back, and the order is updated.

## 6.3 Purchasing process

1. The system shows which products are running low.
2. Management decides what and how much to order.
3. A purchase order is sent to the factory or printer.
4. When the goods arrive, the warehouse checks them and adds them to stock.

## 6.4 Drop process

1. Marketing and management plan a new collection and its release date.
2. New products are added to the system with sizes, colours and prices.
3. Marketing promotes the drop on social media.
4. On drop day, many orders come in at once, and the order process above takes over.

# 7. Focus of the project

The main focus of the project is **data**: how the company stores, connects and uses its information. Laudon and Traver (2021) point out that in e-commerce, the company's data about customers, products and orders is one of its most valuable resources. Chaffey (2015) also stresses that online businesses need their systems to work together so that the customer gets a smooth experience.

For this course, we will focus most on:

- **Orders and customers.** Who buys what, and when.
- **Products and stock.** Sizes, colours and how many are left.
- **Returns and suppliers.** What comes back, and what we buy in.

These areas give us plenty of material for later labs, where we will design data models and a database for Kollekt Studio.

# 8. Summary

Kollekt Studio is a small online streetwear brand that has grown faster than its systems. Our project, *One Place*, will gather all important company data into one shared system. This will help the company avoid overselling, give customers faster answers, make packing quicker and give management better reports. We will keep using Kollekt Studio as our company for the rest of the course.

# References

Chaffey, D. (2015). *Digital Business and E-Commerce Management* (6th ed.). Pearson Education.

Dumas, M., La Rosa, M., Mendling, J., & Reijers, H. A. (2018). *Fundamentals of Business Process Management* (2nd ed.). Springer.

European Union. (2016). *Regulation (EU) 2016/679 of the European Parliament and of the Council (General Data Protection Regulation)*. Official Journal of the European Union, L 119.

Freeman, R. E. (1984). *Strategic Management: A Stakeholder Approach*. Pitman.

Laudon, K. C., & Traver, C. G. (2021). *E-commerce 2021: Business, Technology, Society* (16th ed.). Pearson.

Mintzberg, H. (1979). *The Structuring of Organizations*. Prentice-Hall.
