export interface Ingredient {
    name: string;
    amount: number | null; // Amount can be a number or null
    unit: string | null; // Unit can be a string or null (for items without a unit)
}

export interface Receipt {
    id: number;
    title: string;
    photo_url: string;
    ingredients: Ingredient[]; // Changed from string[] to Ingredient[]
    preparation_steps: string[]; // Changed from string to string[] for separate steps
    tags: string[];
    date_added: string; // Assuming date is in string format (e.g., ISO 8601)
    date_cooked: string | null; // Allows for null value
    rating: number | null; // Allows for null value
    default_servings: number; // Added default_servings to reflect your changes
}
