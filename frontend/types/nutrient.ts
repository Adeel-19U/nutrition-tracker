export interface NutrientCategory {
  id: string;
  name: string;
  slug: string;
}

export interface NutrientGroup {
  id: string;
  name: string;
  slug: string;
}

export interface Unit {
  id: string;
  name: string;
  symbol: string;
}

export interface NutrientTag {
  id: string;
  name: string;
  slug: string;
}

export interface NutrientAlias {
  id: string;
  alias: string;
}

export interface Nutrient {
  id: string;

  name: string;

  slug: string;

  display_name: string | null;

  description: string | null;

  is_essential: boolean;

  daily_recommended_value:
    number | null;

  category: NutrientCategory;

  group: NutrientGroup;

  unit: Unit;

  aliases: NutrientAlias[];

  tags: NutrientTag[];
}