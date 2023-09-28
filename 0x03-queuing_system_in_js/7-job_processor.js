import { createQueue } from 'kue';
const queue = createQueue();

const blacklist = ['4153518780', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100);
  if (blacklist.includes(phoneNumber)) {
    const errMessage = `Phone number ${phoneNumber} is blacklisted`;
    done(new Error(errMessage));
  } else {
    job.progress(50, 100);
    console.log(
      `Sending notification to ${phoneNumber}, with message: ${message}`
    );
    done();
  }
};

// Process 2 jobs concurrently in queue
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
