/*
  Warnings:

  - You are about to drop the column `exerciseId` on the `LiftActivity` table. All the data in the column will be lost.
  - You are about to drop the column `sportsActivityId` on the `SportActivity` table. All the data in the column will be lost.
  - Added the required column `liftExerciseId` to the `LiftActivity` table without a default value. This is not possible if the table is not empty.
  - Added the required column `sportExerciseId` to the `SportActivity` table without a default value. This is not possible if the table is not empty.

*/
-- DropForeignKey
ALTER TABLE "LiftActivity" DROP CONSTRAINT "LiftActivity_exerciseId_fkey";

-- DropForeignKey
ALTER TABLE "SportActivity" DROP CONSTRAINT "SportActivity_sportsActivityId_fkey";

-- AlterTable
ALTER TABLE "LiftActivity" DROP COLUMN "exerciseId",
ADD COLUMN     "liftExerciseId" TEXT NOT NULL;

-- AlterTable
ALTER TABLE "SportActivity" DROP COLUMN "sportsActivityId",
ADD COLUMN     "sportExerciseId" TEXT NOT NULL;

-- AddForeignKey
ALTER TABLE "LiftActivity" ADD CONSTRAINT "LiftActivity_liftExerciseId_fkey" FOREIGN KEY ("liftExerciseId") REFERENCES "LiftExercise"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "SportActivity" ADD CONSTRAINT "SportActivity_sportExerciseId_fkey" FOREIGN KEY ("sportExerciseId") REFERENCES "SportExercise"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
