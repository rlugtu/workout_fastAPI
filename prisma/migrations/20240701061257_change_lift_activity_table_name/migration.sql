/*
  Warnings:

  - You are about to drop the `LiftingActivity` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropForeignKey
ALTER TABLE "LiftingActivity" DROP CONSTRAINT "LiftingActivity_workoutId_fkey";

-- DropTable
DROP TABLE "LiftingActivity";

-- CreateTable
CREATE TABLE "LiftActivity" (
    "id" TEXT NOT NULL,
    "sets" INTEGER NOT NULL,
    "reps" INTEGER NOT NULL,
    "weight" INTEGER NOT NULL,
    "notes" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,
    "deletedAt" TIMESTAMP(3),
    "workoutId" TEXT NOT NULL,

    CONSTRAINT "LiftActivity_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "LiftActivity" ADD CONSTRAINT "LiftActivity_workoutId_fkey" FOREIGN KEY ("workoutId") REFERENCES "Workout"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
