import kue from 'kue';

const queue = kue.createQueue();

const jobDate = {
  phoneNumber: '1234567890',
  message: 'Hello, this is a notification message'
};

const job = queue.create('push_notification_code', jobDate)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });

job.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', (err) => {
  console.log('Notification job failed');
});
