# 📘 Requirements Documentation – Best Practices Guide

## Purpose of This Document
This document defines **how requirements should be structured, split, and consumed** in a modern software development process, with special consideration for:

- complex systems that include both frontend and backend systems
- QA and testability
- AI coding agents and token efficiency
- long-term maintainability

The goal is **clarity without bloat** and **structure without rigidity**.

---

## 1. Core Principles

### 1.1 One Canonical Source of Truth
There must be **one authoritative place** where system behavior is defined.

- Prevents contradictions
- Enables traceability
- Allows safe refactoring

> Everything else (tickets, tests, AI prompts) **derives from or references** this source.

---

### 1.2 Structure Prevents Bloat — Duplication Creates It
Large documents are not a problem.  
**Unstructured documents are.**

Bloat comes from:
- repeating rules
- mixing concerns
- describing visuals in prose
- scattering decisions across tools

---

### 1.3 Requirements Describe Behavior, Not Implementation
Requirements define:
- what the system must do
- under which conditions
- how it behaves at boundaries

They do **not** define:
- frameworks
- components
- internal architecture

---

## 2. One Document vs Multiple Documents

### Best Practice
✅ **One primary requirements document**  
➕ Optional secondary documents only when justified

---

### Why NOT many independent documents
❌ One doc per sprint  
❌ One doc per ticket  
❌ One doc per random feature with no hierarchy  

These lead to:
- fragmentation
- contradictions
- unclear ownership of truth

---

### Why ONE primary document works
- Easier onboarding
- One behavioral contract
- Clear evolution over time
- Easy to version with code

---

### When splitting is justified
Split **only** when:
1. Audience differs (e.g. compliance vs engineering)
2. Change velocity differs greatly
3. Scope becomes unmanageable *in practice*

Splitting is a **reaction to real pain**, not a precaution.

---

## 3. Feature-Based Documentation (Primary Axis)

### Definition
A **feature** describes *what the user can do* and *what the system must support*.

Examples:
- Todo management
- Authentication
- Search & filtering

---

### Why feature-based beats screen-based

| Feature-based | Screen-based |
|--------------|-------------|
| Survives UI changes | Breaks on redesign |
| Maps to backend logic | UI-only |
| Testable | Hard to test |
| AI-agent friendly | UI-scaffold friendly |

> **Features outlive screens. Screens are implementations.**

---

### Best Practice
✅ **Features are the canonical unit of requirements**  
❌ Screens must never redefine feature rules

---

## 4. Screen / View Documentation (Secondary Axis)

### Definition
A **screen/view** describes *where* and *how* features appear.

Screens define:
- layout
- composition
- navigation
- visual states

They do **not** define:
- business rules
- validation logic
- core behavior

---

### When screen-based docs are useful
- frontend-heavy work
- design-driven flows
- AI UI scaffolding
- mobile apps with strong screen boundaries

---

### Best Practice
✅ Screens are **thin adapters** over features  
❌ Screens must never redefine rules

---

## 5. Why Features Are Split into Sections

A feature is **not split into multiple descriptions**.  
It is described **from multiple dimensions**.

Each section answers a different question:

| Question | Section |
|--------|--------|
| Who wants this and why? | User Intent / User Story |
| What must the system do? | Functional Requirements |
| Under what constraints? | Business Rules |
| How does the UI react? | UI Behavior & States |
| What can go wrong? | Error States |
| What quality is required? | Non-Functional Requirements |

This is **classification, not fragmentation**.

---

## 6. UI Behavior & States

### Key Rule
> **Conditional UI logic belongs in UI Behavior & States**

---

## 7. One Doc per Feature vs AI Agents

### Best Practice: Canonical + Sharded
Use one canonical structure with feature-level shards for agent efficiency.

---

## 8. Final Guiding Rules

1. **If it defines behavior → requirements**
2. **If it defines appearance → design**
3. **If it tracks work → tickets**
4. **Features are primary, screens are secondary**
5. **Structure prevents bloat; duplication causes it**
6. **Optimize for humans first, package for agents second**
