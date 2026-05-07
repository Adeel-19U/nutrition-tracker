import { apiFetch } from "@/lib/api";

import { Nutrient } from "@/types/nutrient";


export async function getNutrients() {

  return apiFetch<Nutrient[]>(
    "/nutrients/"
  );
}