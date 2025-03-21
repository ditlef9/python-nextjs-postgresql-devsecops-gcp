// app/(private)/users/[userId]/edit/page.tsx
'use client';

import { useSession } from 'next-auth/react';
import { useParams } from 'next/navigation';
import { useState, useEffect, ChangeEvent, FormEvent } from 'react';

export default function EditUser() {
    // Always call hooks first
    const { data: session } = useSession();
    const { userId } = useParams();

    const [formData, setFormData] = useState({
        user_email: '',
        user_first_name: '',
        user_middle_name: '',
        user_last_name: '',
        user_display_name: '',
        user_is_approved: '',
        user_rank: '',
        user_department: '',
        user_type: ''
    });

    const [feedbackMessage, setFeedbackMessage] = useState('');
    const [feedbackType, setFeedbackType] = useState('');

    // Fetch user data when session and userId are available
    useEffect(() => {
        if (!session || !userId) return; // Ensure session exists before fetching

        const fetchUserData = async () => {
            try {
                const response = await fetch(
                    `${process.env.NEXT_PUBLIC_BACKEND_API_URL}/api/users/get-user/${userId}`,
                    {
                        method: 'GET',
                        headers: {
                            'Content-Type': 'application/json',
                            'Authorization': `Bearer ${session.user.token}`
                        }
                    }
                );

                const data = await response.json();
                if (response.ok) {
                    setFormData({
                        user_email: data.data.user_email,
                        user_first_name: data.data.user_first_name,
                        user_middle_name: data.data.user_middle_name,
                        user_last_name: data.data.user_last_name,
                        user_display_name: data.data.user_display_name,
                        user_is_approved: data.data.user_is_approved ? 'true' : 'false',
                        user_rank: data.data.user_rank,
                        user_department: data.data.user_department,
                        user_type: data.data.user_type
                    });
                } else {
                    setFeedbackMessage(data.message || 'Failed to fetch user data.');
                    setFeedbackType('error');
                }
            } catch (error) {
                console.log('Error fetching user data:', error);
                setFeedbackMessage('Failed to load user data. Please try again later.');
                setFeedbackType('error');
            }
        };

        fetchUserData();
    }, [userId, session]);

    // Now we can safely use conditional rendering
    if (!session) return <p>You must be logged in to view this page.</p>;
    if (session?.user?.rank !== 'admin') return <p>Admin only.</p>;

    const handleChange = (e: ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleCheckboxChange = (e: ChangeEvent<HTMLInputElement>) => {
        setFormData({ ...formData, [e.target.name]: e.target.checked ? 'true' : 'false' });
    };

    const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        setFeedbackMessage('');
        setFeedbackType('');

        try {
            const response = await fetch(
                `${process.env.NEXT_PUBLIC_BACKEND_API_URL}/api/users/edit-user/${userId}`,
                {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${session?.user?.token}`
                    },
                    body: JSON.stringify(formData)
                }
            );

            const data = await response.json();
            if (response.ok) {
                setFeedbackMessage(data.message || 'Successful!');
                setFeedbackType('success');
            } else {
                setFeedbackMessage(data.message || 'Failed.');
                setFeedbackType('error');
            }
        } catch (e) {
            console.log(`[userId]/edit·An error occurred: ${e}`);
            setFeedbackMessage('An error occurred. Please try again.');
            setFeedbackType('error');
        }
    };

    return (
        <>
            <h1>Edit User</h1>
            {feedbackMessage && <div className={feedbackType}><p>{feedbackMessage}</p></div>}

            <form onSubmit={handleSubmit}>
                <p>
                    <label>Email</label><br />
                    <input
                        name="user_email"
                        type="email"
                        value={formData.user_email}
                        onChange={handleChange}
                        required
                        style={{ width: "98%" }}
                        autoFocus
                    />
                </p>
                <p>
                    <label>First Name</label><br />
                    <input
                        name="user_first_name"
                        value={formData.user_first_name}
                        onChange={handleChange}
                        required
                        style={{ width: "98%" }}
                    />
                </p>
                <p>
                    <label>Middle Name</label><br />
                    <input
                        name="user_middle_name"
                        value={formData.user_middle_name}
                        onChange={handleChange}
                        style={{ width: "98%" }}
                    />
                </p>
                <p>
                    <label>Last Name</label><br />
                    <input
                        name="user_last_name"
                        value={formData.user_last_name}
                        onChange={handleChange}
                        required
                        style={{ width: "98%" }}
                    />
                </p>
                <p>
                    <label>Display Name</label><br />
                    <input
                        name="user_display_name"
                        value={formData.user_display_name}
                        onChange={handleChange}
                        required
                        style={{ width: "98%" }}
                    />
                </p>
                <p>
                    <label>User Rank</label><br />
                    <select
                        name="user_rank"
                        value={formData.user_rank}
                        onChange={handleChange}
                        required
                        style={{ width: "98%" }}
                    >
                        <option value="">Select Rank</option>
                        <option value="admin">Admin</option>
                        <option value="user">User</option>
                    </select>
                </p>
                <p>
                    <label>Department</label><br />
                    <input
                        name="user_department"
                        value={formData.user_department}
                        onChange={handleChange}
                        style={{ width: "98%" }}
                    />
                </p>
                <p>
                    <label>User Type</label><br />
                    <select
                        name="user_type"
                        value={formData.user_type}
                        onChange={handleChange}
                        required
                        style={{ width: "98%" }}
                    >
                        <option value="">Select User Type</option>
                        <option value="user">User</option>
                        <option value="service account">Service Account</option>
                    </select>
                </p>
                <p>
                    <label>Approved ({formData.user_is_approved})</label><br />
                    <input
                        type="checkbox"
                        name="user_is_approved"
                        checked={formData.user_is_approved === 'true'}
                        onChange={handleCheckboxChange}
                    />
                </p>

                <p>
                    <button type="submit" className="submit-button">Update User</button>
                </p>
            </form>
        </>
    );
}
