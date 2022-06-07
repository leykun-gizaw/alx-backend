/**
 * @module 6-job_processor
 */
import kue from 'kue';

/* eslint camelcase: 0 */

// Create a kue instance (pun intended)
const push_notification_code = kue.createQueue();

/**
 * @function sendNotification
 * @summary blah blah
 * @param {string} phoneNumber
 * @param {string} message
 */
function sendNotification(phoneNumber, message) {
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`,
  );
}

push_notification_code.process('notification', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});
