# Lecture 31: Unsupervised Machine Learning (Part-1) — Clustering Algorithms Suite

[![Status](https://img.shields.io/badge/Status-Complete-success.svg)](#)
[![Hinglish Version](https://img.shields.io/badge/Notes-Hinglish-yellow.svg)](README_HINGLISH.md)
[![Practice Suite](https://img.shields.io/badge/Practice-Problems-orange.svg)](Practice_Problems/Questions/README.md)
[![Solutions Suite](https://img.shields.io/badge/Practice-Solutions-green.svg)](Practice_Problems/Solutions/README.md)

---

## 📌 Curriculum Overview
Welcome to **Lecture 31: Unsupervised Machine Learning (Part-1)**! This module covers the foundational principles, mathematical formulations, and production implementations of unsupervised clustering techniques.

Topics range from **K-Means**, **Elbow Method**, and **Silhouette Analysis**, to **K-Means++ Initialization**, **Hierarchical Agglomerative Clustering**, **Dendrogram Cutting**, and **DBSCAN Density-Based Outlier Detection**.

---

## 📚 Submodules Directory

| Module Directory | Topic Description | Notes (Dual Language) | Vector PDFs | Runnable Notebook |
| :--- | :--- | :--- | :--- | :--- |
| **Notes_31.01** | **Introduction to Unsupervised Machine Learning** | [English](Notes_31.01/README.md) \| [Hinglish](Notes_31.01/README_HINGLISH.md) | [PDF](Notes_31.01/notes.pdf) \| [PDF (Hi)](Notes_31.01/notes_hinglish.pdf) | — |
| **Notes_31.02** | **What is Clustering — Principles & Distance Metrics** | [English](Notes_31.02/README.md) \| [Hinglish](Notes_31.02/README_HINGLISH.md) | [PDF](Notes_31.02/notes.pdf) \| [PDF (Hi)](Notes_31.02/notes_hinglish.pdf) | — |
| **Notes_31.03** | **K-Means Clustering — Mechanics & Centroid Math** | [English](Notes_31.03/README.md) \| [Hinglish](Notes_31.03/README_HINGLISH.md) | [PDF](Notes_31.03/notes.pdf) \| [PDF (Hi)](Notes_31.03/notes_hinglish.pdf) | — |
| **Notes_31.04** | **Elbow Method for Choosing Optimal K** | [English](Notes_31.04/README.md) \| [Hinglish](Notes_31.04/README_HINGLISH.md) | [PDF](Notes_31.04/notes.pdf) \| [PDF (Hi)](Notes_31.04/notes_hinglish.pdf) | — |
| **Notes_31.05** | **Silhouette Score for Choosing Optimal K** | [English](Notes_31.05/README.md) \| [Hinglish](Notes_31.05/README_HINGLISH.md) | [PDF](Notes_31.05/notes.pdf) \| [PDF (Hi)](Notes_31.05/notes_hinglish.pdf) | — |
| **Notes_31.06** | **Random Initialization Trap & K-Means++** | [English](Notes_31.06/README.md) \| [Hinglish](Notes_31.06/README_HINGLISH.md) | [PDF](Notes_31.06/notes.pdf) \| [PDF (Hi)](Notes_31.06/notes_hinglish.pdf) | — |
| **Notes_31.07** | **K-Means Clustering — Scikit-Learn Implementation** | [English](Notes_31.07/README.md) \| [Hinglish](Notes_31.07/README_HINGLISH.md) | [PDF](Notes_31.07/notes.pdf) \| [PDF (Hi)](Notes_31.07/notes_hinglish.pdf) | [lecture_31_07.ipynb](Notes_31.07/lecture_31_07.ipynb) |
| **Notes_31.08** | **Choosing K (Code) — Elbow & Silhouette Implementation** | [English](Notes_31.08/README.md) \| [Hinglish](Notes_31.08/README_HINGLISH.md) | [PDF](Notes_31.08/notes.pdf) \| [PDF (Hi)](Notes_31.08/notes_hinglish.pdf) | [lecture_31_08.ipynb](Notes_31.08/lecture_31_08.ipynb) |
| **Notes_31.09** | **K-Means Clustering on the Iris Dataset** | [English](Notes_31.09/README.md) \| [Hinglish](Notes_31.09/README_HINGLISH.md) | [PDF](Notes_31.09/notes.pdf) \| [PDF (Hi)](Notes_31.09/notes_hinglish.pdf) | [lecture_31_09.ipynb](Notes_31.09/lecture_31_09.ipynb) |
| **Notes_31.10** | **Hierarchical Clustering — Agglomerative vs Divisive** | [English](Notes_31.10/README.md) \| [Hinglish](Notes_31.10/README_HINGLISH.md) | [PDF](Notes_31.10/notes.pdf) \| [PDF (Hi)](Notes_31.10/notes_hinglish.pdf) | — |
| **Notes_31.11** | **What is a Dendrogram — Structure & Cutting Thresholds** | [English](Notes_31.11/README.md) \| [Hinglish](Notes_31.11/README_HINGLISH.md) | [PDF](Notes_31.11/notes.pdf) \| [PDF (Hi)](Notes_31.11/notes_hinglish.pdf) | — |
| **Notes_31.12** | **Hierarchical Clustering (Code) — Scipy & Scikit-Learn** | [English](Notes_31.12/README.md) \| [Hinglish](Notes_31.12/README_HINGLISH.md) | [PDF](Notes_31.12/notes.pdf) \| [PDF (Hi)](Notes_31.12/notes_hinglish.pdf) | [lecture_31_12.ipynb](Notes_31.12/lecture_31_12.ipynb) |
| **Notes_31.13** | **K-Means vs Hierarchical Clustering — Comparison** | [English](Notes_31.13/README.md) \| [Hinglish](Notes_31.13/README_HINGLISH.md) | [PDF](Notes_31.13/notes.pdf) \| [PDF (Hi)](Notes_31.13/notes_hinglish.pdf) | — |
| **Notes_31.14** | **DBSCAN Clustering — Density-Based Spatial Clustering** | [English](Notes_31.14/README.md) \| [Hinglish](Notes_31.14/README_HINGLISH.md) | [PDF](Notes_31.14/notes.pdf) \| [PDF (Hi)](Notes_31.14/notes_hinglish.pdf) | — |
| **Notes_31.15** | **DBSCAN Clustering (Code) — Scikit-Learn Implementation** | [English](Notes_31.15/README.md) \| [Hinglish](Notes_31.15/README_HINGLISH.md) | [PDF](Notes_31.15/notes.pdf) \| [PDF (Hi)](Notes_31.15/notes_hinglish.pdf) | [lecture_31_15.ipynb](Notes_31.15/lecture_31_15.ipynb) |
| **Notes_31.16** | **K-Means vs DBSCAN on Non-Linear Shapes** | [English](Notes_31.16/README.md) \| [Hinglish](Notes_31.16/README_HINGLISH.md) | [PDF](Notes_31.16/notes.pdf) \| [PDF (Hi)](Notes_31.16/notes_hinglish.pdf) | [lecture_31_16.ipynb](Notes_31.16/lecture_31_16.ipynb) |

---

## 🎯 3 Strict Case-Based Practice Problems (Syllabus Aligned)

1. **Case Study 1: E-Commerce Retail Customer Segmentation (K-Means & Silhouette Optimization)**:
   - High-dimensional customer purchase history segmentation, mathematical inertia decay, exact Silhouette coefficient calculation, and KneeLocator automation.
2. **Case Study 2: Oncological Gene Expression Microarray (Hierarchical Agglomerative Clustering)**:
   - Cancer subtype discovery, Single vs Complete vs Ward linkage criteria, Chaining phenomenon avoidance, and Dendrogram distance threshold cutting.
3. **Case Study 3: Urban Ride-Sharing GPS Hotspot & Anomaly Detection (DBSCAN vs K-Means)**:
   - Segmenting non-linear curved waterfront passenger streams, Voronoi failure of K-Means, Core/Border/Noise tagging, and Density-Connectivity manifold tracing.

- **Questions**: [Practice Problems Questions (README)](Practice_Problems/Questions/README.md) \| `questions.pdf`
- **Solutions**: [Practice Problems Solutions (README)](Practice_Problems/Solutions/README.md) \| `solutions.pdf`
