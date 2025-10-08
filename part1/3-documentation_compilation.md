# HBnB Technical Documentation

## 1. Introduction

The **HBnB Project** is a web-based platform inspired by Airbnb, designed to allow users to register, create property listings (places), post reviews, and search for available listings.  
This technical document provides a **comprehensive overview of the system architecture**, including the **high-level package design**, **class structure**, and **API interaction flows**.  

The purpose of this document is to serve as a **blueprint** for developers working on HBnB, providing a clear reference for understanding how different layers of the system interact — from user-facing APIs to business logic and data persistence.

---

## 2. High-Level Architecture

The HBnB system follows a **three-layer architecture**:

- **Presentation Layer:** Responsible for handling API requests and responses (Flask API / REST endpoints).
- **Business Logic Layer:** Contains models and application logic that enforce the rules of the system.
- **Persistence Layer:** Manages data storage, using either a relational database or file-based storage system.

### High-Level Package Diagram

```mermaid
graph TD
    A[Presentation Layer<br>(API, Views)] --> B[Business Logic Layer<br>(Models, Services)]
    B --> C[Persistence Layer<br>(Database, Storage Engine)]
    C --> B
    B --> A
