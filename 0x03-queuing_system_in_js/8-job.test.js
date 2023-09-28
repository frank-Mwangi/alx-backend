import createPushNotificationsJobs from "./8-job";
import { createQueue } from "kue";
import { expect } from "chai";

const queue = createQueue();

describe("createPushNotificationsJobs", () => {
  beforeEach(() => {
    queue.testMode.enter();
  });
  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });
});

it("Should throw an error if jobs is not an array", () => {
  expect(() => createPushNotificationsJobs(1, queue)).to.throw(
    "Jobs is not an array"
  );
});

it("Should successfully save jobs provided to it in a queue", () => {
  const jobs = [
    {
      phoneNumber: "4153118782",
      message: "This is the code 4321 to verify your account",
    },
    {
      phoneNumber: "4153718781",
      message: "This is the code 4562 to verify your account",
    },
  ];
  createPushNotificationsJobs(jobs, queue);
  expect(queue.testMode.jobs.length).to.equal(2);
});

it("Should listen for failed, completed and in progress events", () => {
  const jobs = [
    {
      phoneNumber: "4153118782",
      message: "This is the code 4321 to verify your account",
    },
    {
      phoneNumber: "4153718781",
      message: "This is the code 4562 to verify your account",
    },
  ];
  createPushNotificationsJobs(jobs, queue);
  queue.testMode.jobs.forEach((job) => {
    expect(job.listenerCount("failed")).to.equal(1);
    expect(job.listenerCount("complete")).to.equal(1);
    expect(job.listenerCount("progress")).to.equal(1);
  });
});
