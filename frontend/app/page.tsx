import { NutrientExplorer } from "@/components/NutrientExplorer";


export default function HomePage() {

  return (
    <main className="
      min-h-screen
      p-8
    ">

      <h1 className="
        text-4xl
        font-bold
        mb-8
      ">
        Nutrition Tracker
      </h1>

      <NutrientExplorer />

    </main>
  );
}