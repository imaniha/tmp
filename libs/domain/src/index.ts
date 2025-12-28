/**
 * Domain models library
 * 
 * This library contains shared domain models, interfaces, and business logic
 * that can be used across both frontend and backend applications.
 */

// Example: Export domain models
export interface User {
  id: string;
  name: string;
  email: string;
}

export interface ApiResponse<T> {
  data: T;
  message?: string;
  status: number;
}

