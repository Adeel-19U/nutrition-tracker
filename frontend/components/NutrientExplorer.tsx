"use client";

import { useEffect, useState } from "react";

import { getNutrients } from "@/services/nutrients";

import { Nutrient } from "@/types/nutrient";


export function NutrientExplorer() {

  const [
    nutrients,
    setNutrients
  ] = useState<Nutrient[]>([]);

  const [
    loading,
    setLoading
  ] = useState(true);

  useEffect(() => {

    async function load() {

      try {

        const data =
          await getNutrients();

        setNutrients(data);

      } catch (error) {

        console.error(error);

      } finally {

        setLoading(false);
      }
    }

    load();

  }, []);

  if (loading) {

    return (
      <div>
        Loading nutrients...
      </div>
    );
  }

  return (

    <div className="space-y-4">

      {nutrients.map((nutrient) => (

        <div
          key={nutrient.id}
          className="
            border
            rounded-xl
            p-4
          "
        >

          <h2 className="
            text-xl
            font-semibold
          ">
            {nutrient.display_name ||
              nutrient.name}
          </h2>

          <div className="
            text-sm
            opacity-70
          ">
            {nutrient.category.name}
            {" • "}
            {nutrient.group.name}
          </div>

          <div className="mt-2">
            Unit:
            {" "}
            {nutrient.unit.symbol}
          </div>

          {nutrient.daily_recommended_value && (

            <div>
              Daily Target:
              {" "}
              {
                nutrient.daily_recommended_value
              }
              {" "}
              {nutrient.unit.symbol}
            </div>

          )}

          {nutrient.tags.length > 0 && (

            <div className="
              flex
              gap-2
              flex-wrap
              mt-3
            ">

              {nutrient.tags.map((tag) => (

                <span
                  key={tag.id}
                  className="
                    px-2
                    py-1
                    rounded-full
                    border
                    text-xs
                  "
                >
                  {tag.name}
                </span>

              ))}

            </div>

          )}

        </div>

      ))}

    </div>
  );
}