# AI Based Contract Review

## Overview 
This was my Senior Design Project for Auburn University. I was tasked with working with Auburn's Office of Sponsored Programs (OSP) to develop a program that could take in a contract and automatically highlight all instances of problematic language/clauses that are contained within the contract. This program will allow the OSP's contract negotiators to be more efficient in how many contracts they are able to process and ultimately allow Auburn University to fulfill its mission of doubling research expenditures set by President Roberts. This tool is meant to be a home-grown and cost-effective tool that competes with commercial applications such as LegalSifter, Lexion.ai, Cobblestone, etc. Originally this started as a three person group project, but one person quickly dropped the course, and the other person did not *meaningfully* contribute to the codebase. So I present to you **Jarrett's Best Effort: AI Based Contract Review**. This project followed an Agile Software Development Life Cycle with several sprints focusing on delivering the Minimum Viable Product for addressing each of the project's user stories.

## Project Introduction
The Office of Sponsored Programs (OSP) is responsible for the administration of research contracts and grants received by the university. OSP has a team of contract administrators who work with sponsors to negotiate and finalize research contracts. The contract negotiation process is time-consuming and requires careful review of legal and technical terms. Currently, the contract review process is manual and can be subject to numerous errors and inefficiencies.

The number of contracts requiring review and their complexity has grown significantly over the past few years with Auburn’s upward trajectory in research funding. However, the number of staff in OSP has remained stagnant. OSP’s review workload is expected to continue to increase with President Robert’s mission to double research expenditures. Pursuant to item number six of the AU Strategic Plan, Operational Excellence, OSP is interested in developing an AI tool to assist with contract review and negotiation in order to enhance the contract review process. There are multiple commercial options available (LegalSifter, Cobblestone, lexion.ai) but they are not cost-efficient. OSP believes a homegrown tool can be developed that would better address the University’s needs.

The objective of this project is to develop an AI tool that can assist OSP contract negotiators in reviewing and negotiating research contracts. The AI tool will be designed to identify and flag legal and technical issues in the contracts, suggest potential revisions and provide guidance on negotiating terms.

## System Metaphor
This software will assist the Office of Sponsored Programs’ contract negotiators in researching and reviewing new research contracts. The system will assist in contract review by scanning contracts and highlighting language that conflicts with Auburn University’s acceptance criteria. Alongside detecting contractual issues, this program should provide alternative text to replace the problematic language with acceptable language and show Auburn’s justification for making said changes. This program should have the capability to learn from successful contract review negotiations to refine future performance. This program should also have functionality to measure the overall risk of a given contract based on attributes such as scope of work, contract partner, budget amount, quality of terms, etc. Combined, all of these tools will assist OSP’s contract reviewers in quickly identifying, assessing, and countering problematic contract terms, which will greatly increase the overall number of contracts the OSP can process.

## User Stories
### 1. Contract Scanning
- **Summary:** As a contract reviewer, I want a tool that reads agreements to find problematic language so that I can process a greater number of agreements.
- **Description:** This feature should read an agreement and search for problematic language and clauses that may exist. The agreement should be compared to the FAR Matrix and the Contract T&Cs Matrix to flag unacceptable language or clauses for removal.

### 2. Alternative Language
- **Summary:** As a contract reviewer I want a tool that can provide alternative language for problematic language in a contract so that I do not have to manually search for the alternative language
- **Description:** This feature should automatically generate alternative language for the contract reviewer to use when encountering problematic language/clauses. The alternative language should be based on existing approved AU alt language documents.

### 3. Adjustment Justification
- **Summary:** As a contract reviewer, I want a tool that can provide justifications for making changes to a contract so that I can save time editing contracts.
- **Description:** This feature should automatically provide justifications for making changes/removals to an agreement based on Auburn’s T&Cs matrix.

### 4. Adaptive Negotiating
- **Summary:** As a contract reviewer, I want this program to learn from previous negotiations so that it can be more helpful to me in the future.
- **Description:** This feature should look at past negotiations and learn from successes/failures regarding the programs generated response and use successful negotiations to improve future performance. For example, if there is a new Boeing negotiation, then the software would filter/recognize previous negotiations with Boeing.

### 5. Automated Risk Assessment
- **Summary:** As a contract reviewer, I want this program to give me an overall risk factor for a contract so that I can make appropriate risk assessments when negotiations reach an impasse.
- **Description:** This feature should be able to collect all risk factors relevant for a given contract and provide relevant information to assist contract reviewers in a manual risk assessment. This functionality would assist in strategizing and guiding negotiations when there are atypical terms being negotiated.

### 6. User Interface
- **Summary:** As a contract reviewer, I want the user interface to make the contract scanning and analysis process as efficient and user-friendly as possible while maintaining clarity and simplicity.
- **Description:** The user interface should provide an intuitive way of interacting with the components and features of the AI Based Contract Review program
