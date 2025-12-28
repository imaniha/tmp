/**
 * API Client library
 * 
 * This library contains API client code for communicating with the backend.
 * It provides typed HTTP clients and service wrappers.
 */

import { ApiResponse } from '@workspace/domain';

/**
 * Base API client configuration
 */
export interface ApiClientConfig {
  baseUrl: string;
  timeout?: number;
}

/**
 * Example API client class
 */
export class ApiClient {
  constructor(private config: ApiClientConfig) {}

  async get<T>(endpoint: string): Promise<ApiResponse<T>> {
    const response = await fetch(`${this.config.baseUrl}${endpoint}`);
    const data = await response.json();
    return {
      data,
      status: response.status,
    };
  }

  async post<T>(endpoint: string, body: unknown): Promise<ApiResponse<T>> {
    const response = await fetch(`${this.config.baseUrl}${endpoint}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
    });
    const data = await response.json();
    return {
      data,
      status: response.status,
    };
  }
}

