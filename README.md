<img align= right width = 200 src="https://us.v-cdn.net/6031544/uploads/editor/ac/j3835e181avs.gif" alt = "question-mark"/>

<h1>Question Answer Platfrom API</h1>

## Overview
This is a backend APIs for a Question Answer Platfrom, where question and answers form various users captured.


<img width = 200  src="https://www.raulvelazquezphd.com/wp-content/uploads/2017/10/Interview-Questions.gif" alt="Q-A-gif"/>

<h1>Understanding the System</h1>
<h3>Entities for the system.</h3>
<p>This platfrom would have the following high level entities, with following relationship among them. Boradly 1 entity should correspond to 1 table in Database. </p>
<ul>
  <li><strong>Question:</strong> Core Entity of the platform.</li>
  <li><strong>Company:</strong> A Company for which question was asked(if any).</li>
  <li><strong>Topic:</strong> Topic for which a question was being asked eg: Data Structures, Algorithms.</li>
  <li><strong>SubTopic:</strong> A topic can have various subtopics Eg: For topic Data Structure, it can have subtopics like Stack, Queues, Lists etc.</li>
  <li><strong>Answer:</strong> A question can have multiple answers.</li>
  <li><strong>Answer_comments:</strong> User can comment on answer, hence an answer can have multiple comments.</li>
  <li><strong>Question_likes:</strong> User have rights to like a question.</li>
  <li><strong>Question_company_mapping:</strong> A question can be asked for many companies. For example, the same question may be asked by Amazon and Microsoft, To capture this information, we need to have this entity.</li>
  <li><strong>Answer_likes:</strong> User may like an answer to question. This data would be stored in this table.</li>
  <li><strong>Tags:</strong> Not all information can be captured using topic and subtopic, For example while subtopics can be Stacks, Queues and Lists, master list of tags may contain complexities of algorithms which could be O(n), O(logn) etc.</li>
  <li><strong>Question_tags:</strong> A Question can be associated with multiple tags. This table will contain this information.</li>
  <li><strong>Users:</strong> And finally the list of users who is posting Questions/Answers/Likes etc.</li>
</ul>

## Various APIs
<Strong>We are going to build following APIs.</strong>

<ul>
  <li><strong>CRUD APs</strong> for all master data, which includes following entities/tables.
    <ul>
      <li>Company</li>
      <li>Topic</li>
      <li>Subtopics</li>
      <li>Tags</li>
    </ul>
  
  </li>

  <li><strong>/POST </strong>Questions
    <ul>
      <li>Input
        <ul>
          <li>Question Text- Mandatory, Min length 50 char, max length 500 char.</li>
          <li>CompanyId - Optional</li>
          <li>SubtopicID - Mandatory</li>
          <li>Tags - List of tags(Optional)</li>
          <li>UserId - the ID of user submitting the question.</li>
        </ul>
      </li>
      <li>Output
        <ul>
          <li>ID- id of the question saved in database.</li>
        </ul>
      </li>
    </ul>
  </li>
</ul>