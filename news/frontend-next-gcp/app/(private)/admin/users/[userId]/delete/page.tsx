// app/(private)/users/[userId]/delete/page.tsx

'use client';

import { useSession } from 'next-auth/react';
import { useParams } from 'next/navigation';
import { useState, useEffect, ChangeEvent, FormEvent } from 'react';

interface User {
    user_email: string;
    user_first_name: string;
    user_middle_name: string;
    user_last_name: string;
    user_display_name: string;
    user_is_approved: boolean;
    user_rank: string;
    user_department: string;
    user_type: string;
}

export default function DeleteUser() {
    // Hooks must be at the top
    const { data: session } = useSession();
    const { userId } = useParams();

    // State hooks
    const [user, setUser] = useState<User | null>(null);
    const [formData, setFormData] = useState({ user_email: '' });
    const [feedbackMessage, setFeedbackMessage] = useState('');
    const [feedbackType, setFeedbackType] = useState('');

    // Fetch user data when the component mounts
    useEffect(() => {
        const fetchUserData = async () => {
            try {
                const response = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_API_URL}/api/users/get-user/${userId}`, {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${session?.user?.token}`
                    }
                });

                const data = await response.json();
                if (response.ok) {
                    setUser(data.data);
                } else {
                    setFeedbackMessage(data.message || 'Failed to fetch user data.');
                    setFeedbackType('error');
                }
            } catch (error) {
                console.error('Error fetching user data:', error);
                setFeedbackMessage('Failed to load user data. Please try again later.');
                setFeedbackType('error');
            }
        };

        fetchUserData();
    }, [userId, session]);

    // Handle email input
    const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
        setFormData({ user_email: e.target.value });
    };

    // Handle delete submission
    const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        setFeedbackMessage('');
        setFeedbackType('');

        try {
            const response = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_API_URL}/api/users/delete-user/${userId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${session?.user?.token}`
                },
                body: JSON.stringify(formData)
            });

            const data = await response.json();
            if (response.ok) {
                setFeedbackMessage(data.message || 'User deleted successfully!');
                setFeedbackType('success');
            } else {
                setFeedbackMessage(data.message || 'Failed to delete user.');
                setFeedbackType('error');
            }
        } catch (error) {
            console.error(`[userId]/delete · An error occurred:`, error);
            setFeedbackMessage('An error occurred. Please try again.');
            setFeedbackType('error');
        }
    };

    // Conditional rendering instead of early returns
    if (!session) {
        return <p>You must be logged in to view this page.</p>;
    }

    if (session?.user?.rank !== 'admin') {
        return <p>Admin only.</p>;
    }

    return (
        <>
            <h1>Delete User</h1>
            {feedbackMessage && <div className={feedbackType}><p>{feedbackMessage}</p></div>}

            {user ? (
                <p>
                    Are you sure you want to delete the user <b>{user.user_display_name}</b>? <br />
                    Confirm by entering the user&apos;s email: <b>{user.user_email}</b>.
                </p>
            ) : (
                <p>Loading user data...</p>
            )}

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
                    <button type="submit" className="submit-button">Delete User</button>
                </p>
            </form>
        </>
    );
}
