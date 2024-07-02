/*
  Warnings:

  - Added the required column `cardioExerciseId` to the `CardioActivity` table without a default value. This is not possible if the table is not empty.
  - Added the required column `exerciseId` to the `LiftActivity` table without a default value. This is not possible if the table is not empty.
  - Added the required column `sportsActivityId` to the `SportActivity` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "CardioActivity" ADD COLUMN     "cardioExerciseId" TEXT NOT NULL;

-- AlterTable
ALTER TABLE "LiftActivity" ADD COLUMN     "exerciseId" TEXT NOT NULL;

-- AlterTable
ALTER TABLE "SportActivity" ADD COLUMN     "sportsActivityId" TEXT NOT NULL;

-- AddForeignKey
ALTER TABLE "LiftActivity" ADD CONSTRAINT "LiftActivity_exerciseId_fkey" FOREIGN KEY ("exerciseId") REFERENCES "LiftExercise"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "SportActivity" ADD CONSTRAINT "SportActivity_sportsActivityId_fkey" FOREIGN KEY ("sportsActivityId") REFERENCES "SportExercise"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CardioActivity" ADD CONSTRAINT "CardioActivity_cardioExerciseId_fkey" FOREIGN KEY ("cardioExerciseId") REFERENCES "CardioExercise"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
